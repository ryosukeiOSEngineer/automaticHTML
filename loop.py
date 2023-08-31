def loop_and_replace_experiences(df, html_template):
    """
    Loop through the experiences in the dataframe and replace the respective placeholders.
    """
    for index in range(len(df)):
        h3_html, p_html, image_file = experiences_oneword_lst(df, index)
        new_img_tag = f'<img decoding="async" loading="lazy" src="{image_file}" alt="{df.loc[index, "gender"]}, {df.loc[index, "age_group"]}" class="c-balloon__iconImg" width="80px" height="80px">'
        html_template = replace_experience_placeholders(html_template, h3_html, p_html, new_img_tag)
    return html_template