

class CredentialsNotFound(Exception):
    def __init__(self, entity):
        self.entity = entity 
    
    def __call__(self):
        return f"Missing Credential {self.entity} please specify with {self.entity}"