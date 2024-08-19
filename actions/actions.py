from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# 한글 수량을 숫자로 변환하는 함수
def convert_korean_quantity(quantity: Text) -> int:
    quantity_dict = {
        "한": 1, "하나": 1, "둘": 2, "두": 2, "셋": 3, "세": 3,
        "넷": 4, "네": 4, "다섯": 5, "여섯": 6, "일곱": 7,
        "여덟": 8, "아홉": 9, "열": 10
    }
    return quantity_dict.get(quantity, quantity)

class ActionConvertQuantity(Action):

    def name(self) -> Text:
        return "action_convert_quantity"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # 현재 quantity 슬롯의 값 가져오기
        quantity = tracker.get_slot('quantity')
        
        # 수량 변환 함수 호출
        quantity_value = convert_korean_quantity(quantity)
        
        # 슬롯에 변환된 수량을 저장
        return [SlotSet("quantity", quantity_value)]

class ActionHandleMultipleDrinks(Action):

    def name(self) -> Text:
        return "action_handle_multiple_drinks"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # tracker에서 엔터티 정보 추출
        entities = tracker.latest_message['entities']

        # 현재 drinks 슬롯의 값 가져오기
        current_drinks = tracker.get_slot('drinks') or []

        # 음료와 수량을 짝지어 리스트에 추가
        for entity in entities:
            if entity['entity'] == 'drink':
                drink = entity['value']
                # 해당 음료에 대한 수량 찾기
                quantity = next((e['value'] for e in entities if e['entity'] == 'quantity' and e['start'] > entity['start']), 1)
                # 수량 변환 함수 호출
                quantity = convert_korean_quantity(quantity)
                current_drinks.append({"drink": drink, "quantity": quantity})

        # drinks 슬롯에 업데이트된 리스트 저장
        return [SlotSet("drinks", current_drinks)]

class ActionConfirmOrder(Action):

    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # drinks 슬롯에서 현재 주문된 음료 목록 가져오기
        drinks = tracker.get_slot('drinks')
        
        if not drinks:
            dispatcher.utter_message(text="아직 주문된 음료가 없습니다.")
            return []

        # 각 음료와 수량을 문자열로 변환하여 하나의 응답 메시지 생성
        order_summary = ", ".join([f"{item['drink']} {item['quantity']}잔" for item in drinks])
        response_message = f"주문하신 음료는 {order_summary}입니다. 맞으신가요?"

        # 사용자에게 응답 메시지 전송
        dispatcher.utter_message(text=response_message)
        
        return []

class ActionResetSlots(Action):

    def name(self) -> Text:
        return "action_reset_slots"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # 주문이 완료된 후 슬롯 초기화: 모든 음료 관련 슬롯을 None으로 설정
        return [
            SlotSet("drinks", None), 
            SlotSet("drink", None), 
            SlotSet("quantity", None)
        ]
