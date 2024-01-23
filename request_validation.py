from pydantic import ValidationError, BaseModel
import allure


@allure.step("Validate Pet Status")
def validation(result: object, model: BaseModel):
    try:
        model.model_validate(result)
        return True
    except ValidationError:
        print("\n", "Unknown Status")
        return False
