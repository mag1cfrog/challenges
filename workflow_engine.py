import json
from typing import Any, Dict

# Define type for job definitions
JobDefinition = Dict[str, Any]

class WorkflowEngine:
    def __init__(self):
        # Mapping of function names to actual callable methods
        self.function_map = {
            'function_w': self.function_w,
            'function_x': self.function_x,
            'function_y': self.function_y,
            'function_z': self.function_z,
        }

    def execute_job_definition(self, job_def: JobDefinition) -> Any:
        """
        Executes the job definition.
        """
        for func_name, params in job_def.items():
            self._execute_function(func_name, params)

    def _execute_function(self, func_name: str, params: Any) -> Any:
        """
        Recursively executes functions based on the job definition.
        """
        # Handle cases when the function has multiple parameters as a list
        if isinstance(params, list):
            resolved_params = []
            # Resolve each parameter
            for param in params:
                # Check if the parameter is a nested function
                if isinstance(param, dict):
                    # It's a nested function
                    nested_func_name, nested_params = next(iter(param.items()))
                    result = self._execute_function(nested_func_name, nested_params)
                    resolved_params.append(result)
                else:
                    # It's a direct parameter
                    resolved_params.append(param)
            # Execute the current function with resolved parameters
            return self.function_map[func_name](*resolved_params)
        
        # Handle cases when the function has a single parameter
        elif isinstance(params, dict):
            # Single nested function without a list
            nested_func_name, nested_params = next(iter(params.items()))
            result = self._execute_function(nested_func_name, nested_params)
            # Execute the current function with the result of the nested function
            return self.function_map[func_name](result)
        else:
            # Single parameter
            return self.function_map[func_name](params)

    # Mock function implementations
    def function_w(self, *args, **kwargs) -> str:
        log = f"Executing function_w with parameters: {args}"
        print(log)
        # Simulate processing and return a result
        return "result_from_function_w"

    def function_x(self, *args, **kwargs) -> str:
        log = f"Executing function_x with parameters: {args}"
        print(log)
        return "result_from_function_x"

    def function_y(self, *args, **kwargs) -> str:
        log = f"Executing function_y with parameters: {args}"
        print(log)
        return "result_from_function_y"

    def function_z(self, *args, **kwargs) -> str:
        log = f"Executing function_z with parameters: {args}"
        print(log)
        return "result_from_function_z"

# Example usage
if __name__ == "__main__":
    # Example job definition JSON
    job_definition_json = """
    {
        "function_z": [
            "param_4",
            {
                "function_x": {
                    "function_w": [
                        "param_1",
                        "param_2"
                    ]
                }
            },
            {
                "function_y": "param_3"
            }
        ]
    }
    """

    # Parse JSON to dictionary
    job_def = json.loads(job_definition_json)

    # Initialize the workflow engine
    engine = WorkflowEngine()

    # Execute the job definition
    engine.execute_job_definition(job_def)
