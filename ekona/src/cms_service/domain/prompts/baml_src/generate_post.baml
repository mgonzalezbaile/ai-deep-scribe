class Post {
    content string @description("The content of the post in markdown format")
}

function GeneratePost(research_brief: string, findings: string) -> Post {
    client OpenRouter
    prompt #"
        {{ _.role("system") }}
        Your task is to synthesize the provided `Findings` into a comprehensive, well-structured post that directly answers the `Research Brief`.

        **Instructions**:

        1.  **Content and Structure**:
            *   The post must be exclusively based on the information provided in the `Findings`.
            *   Structure the content logically to best answer the `Research Brief`. Use markdown for formatting (`#` for the title, `##` for sections, `###` for subsections).

        2.  **Analysis and Tone**:
            *   Provide a detailed and thorough analysis, incorporating specific facts and data from the `Findings`.
            *   Write in a clear, professional, and objective tone. Do not use self-referential language (e.g., "In this post, I will..." or "As an AI...").

        3.  **Citations**:
            *   You MUST cite your sources. Follow the `Citation Rules` provided below for formatting and placement.

        <Citation Rules>
        - Reassign a citation number to each source that is used in the post ([1], [2], [3], ...) and update its reference in the text.
        - Assign each unique URL a single citation number in your text
        - End with ### Sources that lists each source with corresponding numbers
        - IMPORTANT: Number sources sequentially without gaps (1,2,3,4...) in the final list regardless of which sources you choose
        - Each source should be a separate line item in a list, so that in markdown it is rendered as a list.
        - Example format:
        [1] Source Title: URL
        [2] Source Title: URL
        - Citations are extremely important. Make sure to include these, and pay a lot of attention to getting these right. Users will often use these citations to look into more information.
        </Citation Rules>

        {{ _.role("user") }}
        <Research Brief>
        {{research_brief}}
        </Research Brief>

        <Findings>
        {{findings}}
        </Findings>

        {{ ctx.output_format }}
    "#
}
