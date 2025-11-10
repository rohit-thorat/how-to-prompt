import streamlit as st
import requests
import json
import os
import hashlib
import io
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Prompt Post Creator",
    page_icon="📝",
    layout="wide"
)

# Title
st.title("📝 Webflow Post Creator")
st.markdown("---")

# Webflow API Configuration from environment variables
api_token = os.getenv("WEBFLOW_API_TOKEN")
site_id = os.getenv("WEBFLOW_SITE_ID")
collection_id = os.getenv("WEBFLOW_COLLECTION_ID")
folder_id = os.getenv("WEBFLOW_FOLDER_ID", "")  # Optional folder ID for assets

# Initialize form counter for clearing form fields
if 'form_counter' not in st.session_state:
    st.session_state.form_counter = 0

# Sidebar - Show configuration status
# st.sidebar.header("📝 Recent prompt posts")
# if api_token:
#     st.sidebar.success("✅ API Token loaded")
# else:
#     st.sidebar.error("❌ API Token not found in .env")

# if site_id:
#     st.sidebar.success("✅ Site ID loaded")
# else:
#     st.sidebar.error("❌ Site ID not found in .env")

# if collection_id:
#     st.sidebar.success("✅ Collection ID loaded")
# else:
#     st.sidebar.error("❌ Collection ID not found in .env")

# st.sidebar.markdown("---")
# st.sidebar.info("💡 Configure credentials in `.env` file")

# Main content area
col1, col2 = st.columns(2)

# Left column - Input Image
with col1:
    st.subheader("📷 Input Image")
    input_image = st.file_uploader(
        "Upload Input Image",
        type=["png", "jpg", "jpeg", "gif"],
        key=f"input_image_{st.session_state.form_counter}"
    )
    if input_image:
        st.image(input_image, caption="Input Image", use_container_width=True)

# Right column - Output Image
with col2:
    st.subheader("📸 Output Image")
    output_image = st.file_uploader(
        "Upload Output Image",
        type=["png", "jpg", "jpeg", "gif"],
        key=f"output_image_{st.session_state.form_counter}"
    )
    if output_image:
        st.image(output_image, caption="Output Image", use_container_width=True)

# st.markdown("---")

# Title text field
st.subheader("📌 Title")
title_text = st.text_input(
    "Enter post title",
    placeholder="Enter a title for your post...",
    help="This will be the title/name of your post",
    key=f"title_text_{st.session_state.form_counter}"
)

# Prompt text area
st.subheader("✍️ Prompt")
prompt_text = st.text_area(
    "Enter your prompt",
    height=150,
    placeholder="Enter the prompt text here...",
    help="This will be the main content of your post",
    key=f"prompt_text_{st.session_state.form_counter}"
)

# Tags multiselect
st.subheader("🏷️ Tags")
# Predefined tags as dictionary with id (key) and name (value)
# Customize these with your actual Webflow tag IDs
available_tags = {
"68e60f8a7b266769578b810d":	"Backsplash",
"68e60f8ae127b4069da40773":	"Backyard",
"68e60f8bc74ce270ea46899c":	"Balcony",
"68e60f8240486348f97cfdfd":	"Basement",
"68e60f82a357112c564343ae":	"Bathroom",
"68e60f8847b699cfc4d81a8e":	"Bay Window",
"68e60f80c74ce270ea46880a":	"Bedroom",
"68e60f8f81456bb9544c33e9":	"Bohemian",
"68e60f838d7c3d80aa4d9825":	"Bold Colors",
"68e60f86f69efb6ed0988b59":	"Bookshelf",
"68e60f8a6a980cd2aad0e210":	"Breakfast Nook",
"68e60f90212a74ebb1f40d34":	"Brick",
"68e60f86b27cbe6725a454a2":	"Built-In Shelving",
"68e60f860815a2dc85e91fa2":	"Built-In Storage",
"68e60f8a04046a6389fc36b9":	"Cabinet Makeover",
"68e60f8df7e43d728eacbc6f":	"Cladding",
"68e60f8f71973e06c808ea43":	"Coastal",
"68e60f856128356079d07fa3":	"Color Scheme",
"68e60f901742ca655cb93664":	"Concrete",
"68e60f849b0d71e6a19a8ef2":	"Contemporary",
"68e60f8a02672257a9a79711":	"Countertop",
"68e60f8bf79d154305190119":	"Courtyard",
"68e60f8e73c260618984e4a7":	"Curb Appeal",
"68e60f853e13554af2bb7477":	"Dark Interiors",
"68e60f8b777925e6ffe8022e":	"Deck",
"68e60f8efb9c6fce94d4b18f":	"Deck Railing",
"68e60f81eb6cd9bccb1cdb6e":	"Dining Room",
"68e60f8b5313be5fc090b8fa":	"Driveway",
"68e60f81a2d0b29e2e64bea5":	"Entryway",
"68e60f8d8d7f68f7387f24c3":	"Exterior Lighting",
"68e60f8fec642ec895594e84":	"Farmhouse",
"68e60f8eb40c9c1ee1dfc359":	"Fence",
"68e60f8c3d5b4ef0864d793b":	"Fire Pit",
"68e60f87e129698413ced68b":	"Fireplace",
"68e60f84751353b6b5fa3d32":	"Floor Plan",
"68e60f8c8c56110795269896":	"Fountain",
"68e60f89586e0417d6e499f0":	"French Doors",
"68e60f8add409e3fd1f09237":	"Front Yard",
"68e60f8650036875471f5905":	"Gallery Wall",
"68e60f8b95c57041a72abaa9":	"Garden",
"68e60f8eba47276b95653627":	"Gate",
"68e60f8cb166653a545a4a49":	"Gazebo",
"68e60f909c3dd0b9dfa75c73":	"Glass",
"68e60f809c3dd0b9dfa75981":	"Guest Room",
"68e60f8393b0430469db65ce":	"Gym Room",
"68e60f8114e0fe983accbeac":	"Hallway",
"68e60f81897fe0e1aa4c9c09":	"Home Office",
"68e60f8fcab745cc5c2ed43c":	"Industrial",
"68e60f806a625a4aedfe282d":	"Kids Room",
"68e60f810835a36c0ceb3adc":	"Kitchen",
"68e60f82aedadd0345695055":	"Laundry Room",
"68e60f8cb141d2b1fb9c459c":	"Lawn",
"68e60f86bb4aab134b77ce74":	"Lighting",
"68ff53068d15d9c4d5bf6e2b":	"Listing",
"68e60f802a9cf860d9435607":	"Living Room",
"68e60f828999d40d9d51a9c1":	"Loft",
"68e60f91f7e43d728eacbcfe":	"Marble",
"68e60f82d18d4e3c2f361449":	"Media Room",
"68e60f9198e08190d7875a5f":	"Metal",
"68e60f8f5293cca434731ad9":	"Mid-Century",
"68e60f832fbbb8147d42aa91":	"Minimalist",
"68e60f841742ca655cb93176":	"Modern",
"68e60f92088cac75eddb8930":	"Modern Architecture",
"68e60f83953b960491d924b5":	"Monochrome",
"68e60f82658910466225ddb5":	"Mudroom",
"68e60f85422004a3f19b9ebb":	"Natural Light",
"68e60f88bf0e1972cd7703c6":	"Nursery",
"68e60f8cac3ee1a8ac656cc3":	"Outdoor Kitchen",
"68e60f8df238aa884322e54c":	"Outdoor Seating",
"68e60f89909881683b8083d5":	"Pantry Storage",
"68e60f8d953b960491d926a6":	"Pathway",
"68e60f8bf32596319228acc4":	"Patio",
"68e60f8ceaf65a901ef8ee48":	"Pergola",
"68e60f8cc4ba42c966050398":	"Planters",
"68e60f8cf79d154305190160":	"Pool",
"68e60f8b825dc3467d091a88":	"Porch",
"68e60f8196ea0570d66326fe":	"Powder Room",
"68e60f80f0ff75ae2ae231b6":	"Primary Bedroom",
"68e60f8f107770fb9094de51":	"Rustic",
"68e60f88870c2e8c19d935a3":	"Skylight",
"68e60f845293cca4347317c9":	"Small Space",
"68e60f88f9c18b39b75ce3bd":	"Stairway Design",  
"68e60f9288e6870af3f5e0b6":	"Style Identification",
"68e60f8bf408e2298e724658":	"Terrace",
"68e60f81cbf57a149b6a6848":	"Toddler Room",
"68e60f87d18d4e3c2f361508":	"Tv Placement",
"68e60f88c6c00ab4c0b509fd":	"Vanity",
"68ff52f0269d3943d18b5c2d":	"Virtual Staging",
"68e60f86cf78c699c78b0c33":	"Wardrobe",
"68e60f834afdc80d9f9e1ef1":	"Yoga Room",
}

# Create display options (show names to user)
tag_display_options = list(available_tags.values())

selected_tag_names = st.multiselect(
    "Select tags for your post",
    options=tag_display_options,
    help="Select one or more tags",
    key=f"tags_{st.session_state.form_counter}"
)

# Get the IDs of selected tags
selected_tag_ids = [tag_id for tag_id, tag_name in available_tags.items() if tag_name in selected_tag_names]

# Display selected tags
# if selected_tag_names:
#     st.write("Selected tags:", ", ".join(selected_tag_names))
#     with st.expander("View Tag IDs (for debugging)"):
#         st.code(selected_tag_ids)

st.markdown("---")

# Initialize session state for tracking post success and loading
if 'post_success' not in st.session_state:
    st.session_state.post_success = False
if 'is_posting' not in st.session_state:
    st.session_state.is_posting = False

# Post button or Create New button
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])

with col_btn2:
    if st.session_state.get('post_success', False):
        # Show "Create New" button after successful post
        st.success("✅ Successfully posted to Webflow!")
        if st.button("➕ Create New Post", type="primary", use_container_width=True, key="create_new"):
            # Increment form counter to clear all form fields
            st.session_state.form_counter += 1
            # Reset post states
            st.session_state.post_success = False
            st.session_state.is_posting = False
            st.rerun()
        post_button = False
    elif st.session_state.get('is_posting', False):
        # Show loading button with spinner while posting
        st.button("⏳ Posting...", type="primary", use_container_width=True, disabled=True)
        post_button = False
    else:
        # Show "Post to Webflow" button
        post_button = st.button("🚀 Post to Webflow", type="primary", use_container_width=True)

# Placeholder for status messages
status_placeholder = st.empty()

# Helper function to calculate file hash
def get_file_hash(file_content: bytes) -> str:
    """Calculate SHA-256 hash of file content"""
    return hashlib.sha256(file_content).hexdigest()

# Function to upload image to Webflow using direct API calls
def upload_image_to_webflow(image_file, api_token: str, site_id: str, folder_id: str = None) -> dict:
    """Upload an image to Webflow and return the image data"""
    try:
        # Get file content and calculate hash
        file_content = image_file.getvalue()
        file_hash = get_file_hash(file_content)
        file_name = image_file.name
        
        # Step 1: Initiate the upload with Webflow API
        init_url = f"https://api.webflow.com/v2/sites/65eede53df668d7015c0bd82/assets"
        
        headers = {
        'Authorization': f"Bearer {api_token}",
        'Content-Type': 'application/json'
        }
        
        init_payload = {
            "fileName": file_name,
            "fileHash": file_hash,
            "parentFolder": folder_id
        }
        
        # Initiate upload
        init_response = requests.post(init_url, headers=headers, json=init_payload)
        
        if init_response.status_code not in [200, 201, 202]:
            st.error(f"❌ Failed to initiate upload: {init_response.text}")
            return None
            
        upload_data = init_response.json()
        
        # Step 2: Upload to S3 using the provided details
        upload_url = upload_data.get("uploadUrl")
        upload_details = upload_data.get("uploadDetails")
        hostedUrl = upload_data.get("hostedUrl")
        
        if not upload_url or not upload_details:
            st.error("❌ Invalid upload response from Webflow")
            return None

        # Prepare the form data for S3
        form_data = {
            "acl": upload_details.get("acl"),
            "bucket": upload_details.get("bucket"),
            "X-Amz-Algorithm": upload_details.get("X-Amz-Algorithm"),
            "X-Amz-Credential": upload_details.get("X-Amz-Credential"),
            "X-Amz-Date": upload_details.get("X-Amz-Date"),
            "key": upload_details.get("key"),
            "Policy": upload_details.get("Policy"),
            "X-Amz-Signature": upload_details.get("X-Amz-Signature"),
            "success_action_status": upload_details.get("success_action_status"),
            "Content-Type": upload_details.get("content-type"),
            "Cache-Control": upload_details.get("Cache-Control"),
        }
        # Prepare file for upload
        file_content_io = io.BytesIO(file_content)
        files = {"file": (file_name, file_content_io, upload_details.get("contentType"))}

        # Upload to S3
        upload_response = requests.post(upload_url, data=form_data, files=files)
        
        if upload_response.status_code == 201:
            # st.success(f"✅ Successfully uploaded {file_name}")
            # Return the asset information
            asset_id = upload_data.get("id")
            asset_key = upload_details.get("key")
            return {
                "id": asset_id,
                "url": hostedUrl,
                "file_name": file_name
            }
        else:
            st.error(f"❌ Failed to upload {file_name} to S3. Status: {upload_response.status_code}")
            return None
            
    except Exception as e:
        st.error(f"Error uploading image: {str(e)}")
        return None

# Function to post to Webflow
def post_to_webflow(api_token: str, collection_id: str, data: dict) -> bool:
    """Post data to Webflow collection"""
    try:
        url = f"https://api.webflow.com/v2/collections/{collection_id}/items"
        
        headers = {
            "Authorization": f"Bearer {api_token}",
            "accept": "application/json",
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in [200, 201, 202]:
            return True, response.json()
        else:
            return False, response.text
            
    except Exception as e:
        return False, str(e)

# Handle post submission
if not st.session_state.get('post_success', False) and post_button:
    # Validation
    if not api_token:
        st.error("⚠️ WEBFLOW_API_TOKEN not found in .env file")
    elif not site_id:
        st.error("⚠️ WEBFLOW_SITE_ID not found in .env file")
    elif not collection_id:
        st.error("⚠️ WEBFLOW_COLLECTION_ID not found in .env file")
    elif not input_image:
        st.error("⚠️ Please upload an input image")
    elif not output_image:
        st.error("⚠️ Please upload an output image")
    elif not title_text:
        st.error("⚠️ Please enter a title")
    elif not prompt_text:
        st.error("⚠️ Please enter a prompt")
    else:
        # Set loading state and rerun to show the loading button
        st.session_state.is_posting = True
        st.rerun()

# Continue processing if is_posting is True
if st.session_state.get('is_posting', False) and not st.session_state.get('post_success', False) and input_image and output_image and title_text and prompt_text:
    # Show spinner while uploading images
    with status_placeholder:
        with st.spinner("📤 Uploading images to Webflow..."):
            # Upload images
            input_image_data = upload_image_to_webflow(input_image, api_token, site_id, folder_id)
            output_image_data = upload_image_to_webflow(output_image, api_token, site_id, folder_id)
    
    if not input_image_data or not output_image_data:
        with status_placeholder:
            st.error("❌ Failed to upload images. Please check your credentials and try again.")
        st.session_state.is_posting = False
    else:
        with status_placeholder:
            st.success("✅ Images uploaded successfully!")
        
        # Prepare data for Webflow
        # Note: Adjust field names according to your Webflow collection schema
        post_data = {
            "isArchived": False,
            "isDraft": True,
            "fieldData": {
                "name": title_text,  # Using the title field
                "slug": f"post-{abs(hash(title_text))}",  # Generate slug from title
                "prompt-title": title_text,
                "prompt": prompt_text,
                "prompt-tags": selected_tag_ids,  # Post tag IDs as array
                "input-image": input_image_data.get("url"),
                "output-image": output_image_data.get("url"),
            }
        }
        
        # Show spinner while posting to Webflow
        with status_placeholder:
            with st.spinner("🚀 Posting to Webflow..."):
                success, response = post_to_webflow(api_token, collection_id, post_data)
        
        if success:
            with status_placeholder:
                st.success("✅ Successfully posted to Webflow!")
            # st.json(response)
            
            # Reset loading state and set success state
            st.session_state.is_posting = False
            st.session_state.post_success = True
            st.rerun()
        else:
            with status_placeholder:
                st.error(f"❌ Error posting to Webflow: {response}")
                st.info("""
                💡 **Tip**: Make sure the field names in the code match your Webflow collection schema.
                You may need to update the field names in the `post_data` dictionary.
                """)
            st.session_state.is_posting = False

# Footer
# st.markdown("---")
# st.markdown(
#     """
#     <div style='text-align: center; color: gray;'>
#     <small>Made with ❤️ using Streamlit | Powered by Webflow API</small>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

