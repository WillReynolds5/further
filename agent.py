from util.inference import inference
from prompts import FurtherPrompt
import json

class FurtherAgent:
    def __init__(self):
        self.name = "Further Agent"
        self.default_model = "google/gemini-2.0-flash-001"
    
    def respond(self, messages):
        """
        Process incoming messages and return a response using the LLM.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            
        Returns:
            dict: Contains the response message and additional metadata like thinking
        """
        try:
            # Format messages using the FurtherPrompt class
            formatted_messages = FurtherPrompt.format_messages(messages)
            
            # Get response from the LLM
            raw_response = inference(
                messages=formatted_messages,
                model=self.default_model
            )
            
            # Parse the response to extract thinking, action, and parameters
            thinking, action, parameter = FurtherPrompt.parse_response(raw_response)
            
            # Log the action and parameters for debugging
            print(f"Thinking: {thinking}")
            print(f"Action: {action}")
            print(f"Parameters: {parameter}")
                        
            # Process different action types
            if action == 'InformativeResponse':
                response = parameter
                
            elif action == 'NoninformativeResponse':
                response = parameter
                
            elif action == 'RequestInformation':
                response = parameter
                
            elif action == 'ScheduleTour':
                response = f"RUNNING SCHEDULE TOOL W/ PARAMTERS: {parameter}"
                
            elif action == 'CheckAvailability':
                response = parameter
                
            elif action == 'parsing_error':
                # If parsing failed, just return the raw response
                response = raw_response
            else:
                # For other or unknown actions, return a generic response
                response = parameter

            # Return both the final response message and the thinking process
            return {
                "message": response,
                "thinking": thinking,
                "action": action,
                "parameters": parameter
            }
                
        except Exception as e:
            # Fallback response in case of error
            error_message = f"I apologize, but I'm having trouble connecting to my resources right now. Error: {str(e)}"
            return {
                "message": error_message,
                "thinking": None,
                "action": "error",
                "parameters": {"error": str(e)}
            }
