from .errorcodes_constants import GENERIC_ERROR
class GenericError():
    
    def __init__(self) -> None:
        print(f"Error {GENERIC_ERROR} : Operation unsuccessful")
