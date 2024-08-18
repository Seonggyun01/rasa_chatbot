from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionConvertQuantity(Action):

    def name(self) -> Text:
        return "action_convert_quantity"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        quantity = tracker.get_slot('quantity')
        
        # 한글 수량을 숫자로 변환
        quantity_dict = {
            "한": 1,
            "하나": 1,
            "둘": 2,
            "셋": 3,
            "넷": 4,
            "다섯": 5,
            "여섯": 6,
            "일곱": 7,
            "여덟": 8,
            "아홉": 9,
            "열": 10,
            "두": 2,
            "세": 3,
            "네": 4
        }
        
        # 숫자가 아니면서 한글로 된 수량을 변환
        if quantity in quantity_dict:
            quantity_value = quantity_dict[quantity]
        else:
            try:
                # 숫자로 변환 가능한지 확인 (예: '3' -> 3)
                quantity_value = int(quantity)
            except ValueError:
                # 숫자 변환 실패 시, 기본적으로 1로 설정 (필요에 따라 수정 가능)
                quantity_value = 1
                dispatcher.utter_message(text="알 수 없는 수량 입력입니다. 기본 수량 1로 처리됩니다.")
        
        # 슬롯에 변환된 숫자를 저장
        return [SlotSet("quantity", quantity_value)]
