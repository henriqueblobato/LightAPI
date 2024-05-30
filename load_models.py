from atlas_provider_sqlalchemy.ddl import print_ddl

import importlib
import os
from typing import List
from sqlalchemy.ext.declarative import declarative_base

from database import engine

CustomBase = declarative_base()


def load_classes_from_file(file_path: str) -> List[type]:
    """Load all classes from a given Python file."""
    try:
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        attributes = dir(module)
        classes = [getattr(module, attr) for attr in attributes if isinstance(getattr(module, attr), type)]
        sqlalchemy_models = [
            cls for cls in classes
            if hasattr(cls, '__table__')
        ]
        return sqlalchemy_models
    except Exception as e:
        print(f"Error loading classes from file '{file_path}': {e}")
        return []


def load_all_classes(directory: str = "models") -> List[type]:
    """Load all classes from all Python files in a directory."""
    classes = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_classes = load_classes_from_file(file_path)
                classes.extend(file_classes)
    return classes


_models = load_all_classes()
print_ddl(engine.dialect.name, _models)

