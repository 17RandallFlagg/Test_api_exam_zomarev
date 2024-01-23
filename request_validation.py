from pydantic import ValidationError, BaseModel
import allure


@allure.step("Validate Pet Status")
def validation(result: object, model: BaseModel):
    try:
        model.model_validate(result)
        return True
    except ValidationError as e:
        print("\n", "Unknown Pet Status\n", e.json())
        return False
