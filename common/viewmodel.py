from typing import Any

class ViewModel(dict):
    def __init__(self, *args, **kwargs):
        all = {
            'error': None,
            'error_msg': None
        }
        all.update(kwargs)
        super().__init__(self, *args, **all)

    def __getattr__(self, __name: str) -> Any:
        return self[__name]
    
    def __setattr__(self, __name: str, __value: Any) -> Any:
        self[__name] = __value