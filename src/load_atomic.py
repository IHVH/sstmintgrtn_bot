import inspect
import os
from pathlib import Path
from typing import List
from bot_func_abc import AtomicBotFunctionABC


class LoadAtomic():
    @staticmethod
    def load_functions(func_dir:str = "functions", atomic_dir:str = "atomic") -> List[AtomicBotFunctionABC]:
        atomic_func_path = Path.cwd() / "src" / func_dir / atomic_dir
        suffix = ".py"
        lst = os.listdir(atomic_func_path)
        function_objects: List[AtomicBotFunctionABC] = []
        for fn_str in lst:
            if suffix in fn_str:
                mn = fn_str.removesuffix(suffix)
                module = __import__(f"{func_dir}.{atomic_dir}.{mn}", fromlist = ["*"])
                for name, cls in inspect.getmembers(module):
                    if inspect.isclass(cls) and cls.__base__ is AtomicBotFunctionABC:
                        obj: AtomicBotFunctionABC = cls() 
                        function_objects.append(obj)
                        #logger.info(f"Add object - {obj}; From module {module}; Class neme='{name}', ")

        return function_objects
