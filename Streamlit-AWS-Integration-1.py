import streamlit as st
import boto3
import uuid
import json
aws_access_key_id = 'AKIAXYKJUAFGZDCG6MN6'
aws_secret_access_key = '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'
region_name = 'ap-south-1'

#Integrating with aws lambda
lambda_client = boto3.client(
    'lambda',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Streamlit UI components
st.title('Post Composer')

# Input field for text content
post_content = st.text_area('Compose your post:', height=100)



post_data = {
        'post_id': str(uuid.uuid4()), 
        'post': post_content
    }
var1=json.dumps(post_data)

# Button to submit the post
if st.button('Publish to Aws Lambda'):
    # Process the post and hashtags
    response=lambda_client.invoke(
        FunctionName='streamlitfunction',
        Payload=var1
    )
    print(response)
    st.title('Trending Hashtags')
    hashtag_list = []
    for word in var1.split():
        if word[0] == '#':
            hashtag_list.append(word[1:])
    for hashtag in hashtag_list:
        st.write(hashtag)
