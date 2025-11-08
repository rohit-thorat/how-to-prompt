# Webflow Post Creator

A simple Streamlit application to post content to Webflow using their API.

## Features

- 📷 Upload two images (Input and Output)
- ✍️ Text area for prompt/content
- 🏷️ Multi-select tags with custom tag support
- 🚀 Post directly to Webflow via API

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file from the example:
```bash
cp env.example .env
```

3. Edit the `.env` file and add your Webflow credentials:
```
WEBFLOW_API_TOKEN=your_api_token_here
WEBFLOW_SITE_ID=your_site_id_here
WEBFLOW_COLLECTION_ID=your_collection_id_here
```

## Configuration

### Getting Your Webflow Credentials

1. **Webflow API Token**: 
   - Go to your Webflow account settings
   - Navigate to Integrations → API Access
   - Generate a new API token
   - Add it to `.env` as `WEBFLOW_API_TOKEN`

2. **Webflow Site ID**:
   - Go to your Webflow site settings
   - The Site ID can be found in the URL or via the Webflow API
   - Add it to `.env` as `WEBFLOW_SITE_ID`

3. **Collection ID**:
   - In Webflow, go to your CMS Collections
   - Select the collection you want to post to
   - The Collection ID can be found in the URL or via the Webflow API
   - Add it to `.env` as `WEBFLOW_COLLECTION_ID`

### Customizing Field Names

The app uses default field names for the Webflow collection. You may need to update these to match your collection schema:

- Edit `webflow_post.py`
- Find the `post_data` dictionary (around line 206)
- Update the field names to match your Webflow collection fields

### Configuring Tags

Tags are stored as a dictionary with IDs (keys) and names (values):

1. Get your tag IDs from Webflow:
   - Use the Webflow API to list your collection's reference fields
   - Or find them in your Webflow CMS settings

2. Update the `available_tags` dictionary in `webflow_post.py` (around line 87):
```python
available_tags = {
    "actual_tag_id_1": "Tag Name 1",
    "actual_tag_id_2": "Tag Name 2",
    # Add your actual Webflow tag IDs and names
}
```

3. The app will:
   - Display tag names to users in the multiselect
   - Post only the tag IDs to Webflow (as an array)

## Usage

1. Run the Streamlit app:
```bash
streamlit run webflow_post.py
```

2. The sidebar will show the status of your environment variables

3. Fill in the form:
   - Upload an input image
   - Upload an output image
   - Enter your prompt text
   - Select tags (or add custom tags)

4. Click "Post to Webflow" to submit

## API Documentation

For more information about the Webflow API, visit:
- [Webflow API Documentation](https://developers.webflow.com/)
- [Webflow API v2 Reference](https://developers.webflow.com/v2.0.0/reference)

## Security

- Never commit your `.env` file to version control
- The `.env` file is already in `.gitignore` by default
- Keep your API tokens secure and rotate them regularly

## Notes

- The app will automatically upload images and post to Webflow when you click the button
- Ensure your API token has the necessary permissions for:
  - Uploading assets to your site
  - Creating items in your collection
- Field names in the code may need to be adjusted to match your Webflow collection schema

