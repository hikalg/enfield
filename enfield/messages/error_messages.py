class GenericError():
    
    error_code : int = -1
    
    def __str__(self) -> str:
        return f"Error {self.error_code} Operation unsucessful"