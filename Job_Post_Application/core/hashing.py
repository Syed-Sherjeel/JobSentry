from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)


if __name__ == "__main__":
    hasher = Hasher()
    print(hasher.get_password_hash("123456"))
    print(hasher.verify_password("HelloWorld", "$2y$12$kbQm9Vb96023efZFhSkZf.a4bAGyzDW6zKC/K1JDtKY0f.gKZxAHO"))
