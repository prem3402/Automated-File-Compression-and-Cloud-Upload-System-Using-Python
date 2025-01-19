<h1> Automated File Compression and Cloud Upload System Using Python (Automated Backup Tool) </h1>
<p>This project is a Python-based system that automates file compression and uploads the compressed archive to a Windows shared drive and optionally to Google Drive. It utilizes SMB protocol for Windows share operations and Google Drive API for cloud uploads.</p>
<hr>
<h2>Features</h2>
<ol type="1">
    <li>Compress Files:</li>
    <ul type="disc">
    <li>Compresses files and directories into a zip archive with the current date as part of the filename.</li>
    <li>Deletes original files and folders after compression.</li>
    </ul>
    <li>Upload to Windows Shared Drive:</li>
    <ul type="disc">
        <li>Uploads the compressed zip archive to a specified remote Windows shared folder using SMB protocol.</li>
    </ul>
    <li>Upload to Google Drive:</li>
    <ul type="disc">
        <li>Optionally uploads the zip archive to a specified folder in Google Drive.</li>
    </ul> 
</ol>
<hr>
<h2>Prerequisites</h2>
 <ol type="1">
    <li><b>Python:</b> Ensure Python 3.7 or higher is installed.
</li>
    <li><b>Google Cloud Credentials:</b></li>
    <ul type="disc">
    <li> Obtain a <b><u>client_secrets.json</b></u> file from your Google Cloud Console.</li>
    <li>Enable the Google Drive API for your project.</li>
    </ul>
<li><b>Windows Shared Drive Access:</b> Ensure you have the correct credentials and permissions to access the remote shared folder.</li>
</ol>
<hr>
<h2>Setup</h2>
 <h3> Step 1: Clone the Repository</h3>

git clone https://github.com/prem3402/Automated-File-Compression-and-Cloud-Upload-System-Using-Python.git

cd Automated-File-Compression-and-Cloud-Upload-System-Using-Python

<h3>Step 2: Install the Dependencies</h3>

pip install -r requirements.txt

<h3>Step 3: Configure the Credentials</h3>
<ol type="1">
<li>Place your Google Drive API credentials (client_secrets.json) in the project directory.</li>
<li>Ensure access to the remote Windows shared drive with correct username and password.</li>

<h3>Step 4: Run the Script</h3>
Modify the input_paths, remote_computer, shared_folder, destination_path, user_name, user_password, and other parameters in the script as needed. Then, execute:
```bash
python main.py
```
