class ClarificationResponse {
    need_clarification bool @description("If you need to ask a clarifying question, return 'True'. Otherwise, return 'False'.")
    question string @description("The question to ask the user to clarify the topic of the post")
    verification string @description("The verification message that we will start research")
}

function AskForClarification(messages: string, date: string) -> ClarificationResponse {
    client OpenRouter
    prompt #"
        {{ _.role("system") }}
        You are a copywriter assistant that helps the user to create a post.
        Your goal now is to ensure that you have enough information about the topic of the post.

        {{ _.role("user") }}
        These are the messages that have been exchanged so far from the user asking for the post:
        {{messages}}

        Today's date is {{date}}. 

        Assess whether you need to ask a clarifying question, or if the user has already provided enough information about the topic of the post.

        If there are acronyms, abbreviations, or unknown terms, ask the user to clarify.
        If you need to ask a question, follow these guidelines:
        - Be concise while gathering all necessary information
        - Make sure to gather all the information needed to start working on the post.
        - Use bullet points or numbered lists if appropriate for clarity. Make sure that this uses markdown formatting and will be rendered correctly if the string output is passed to a markdown renderer.
        - Don't ask for unnecessary information, or information that the user has already provided. If you can see that the user has already provided the information, do not ask for it again.
    {{ ctx.output_format }}
    "#
}
