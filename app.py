import base64
from github import Github

GITHUB_TOKEN = st.secrets['GITHUB_TOKEN']

def upload_to_github(file_name, file_content, repo, path):
    g = Github(GITHUB_TOKEN)
    repository = g.get_repo(repo)
    repository.create_file(path, 'Upload: ' + file_name, file_content, branch='main')


def render_upload():
    uploaded_file = st.file_uploader('Upload a file', type=['pdf', 'py', 'txt', 'xlsx', 'csv', 'json'], accept_multiple_files=True)
    if uploaded_file is not None:
        for file in uploaded_file:
            file_name = file.name
            file_content = base64.b64encode(file.read()).decode()  # Encode file content in base64
            repo = "user/repo"  # Change to your repo
            path = f'uploads/{file_name}'  # Define path in repo
            upload_to_github(file_name, file_content, repo, path)
            st.success(f'{file_name} uploaded successfully!')


def main():
    st.title('My App')
    # Existing UI code here...
    if st.button('Upload Section'):
        render_upload()  # Integrate upload section into the main app layout

    # Existing routing code here...


if __name__ == '__main__':
    main()