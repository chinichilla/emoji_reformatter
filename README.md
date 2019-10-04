# Emoji Renamer (Custom Slack Emoji Renaming in Bulk for Non-Admins)

Guide to export and import your custom emojis from one slack workspace to another without being an admin. This renamer currently supports jpg, gif, and png. Let me know if you'd like more file types, and I'll update the python function. 

## Export Your Emojis in Bulk from the Old Workspace

1. Install [Save All Resources](https://chrome.google.com/webstore/detail/save-all-resources/abpdnfjocnmdomablahdcfnoggeeiedb?hl=en-US) on Chrome extension.

2. Open your Developer Tools window on Chrome using Ctrl Shift J (on Windows), Ctrl Option J (on Mac), or Chrome's More Tools.

3. Click on "ResourceSaver." Now you can download your resource files from your Custom Slack Emoji page.

4. Navigate to your workspace's custom emoji page: <https://[workspace_name].slack.com/customize/emoji>.

5. Now scroll all the way through your workspace's emojis. This will store them in your /top/emoji.slack-edge.com/T024FPYBQ/ folder. You can view it by going to the "Sources" tab in Developer Tools.

6. Once you have collected all the emojis, click Download on the "ResourcesSaver" tab. 

### Using the Emoji Renamer 

We'll now use Emoji Renamer to rename the files with their original workspace's names. 

1. Now `github-clone` the repo.

2. Rename **T024FPYBQ** to **emojis**.

3. Place **emojis** inside the **emoji_renamer** directory.

4. Run `python emoji_renamer.py`. This will create a folder called **new_emojis**.

## Import Your Emojis in Bulk into the New Workspace

1. Download the [Neutral Face Emoji Tools](https://chrome.google.com/webstore/detail/neutral-face-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej) Chrome extension.

2. Navigate to your second workspace's custom emoji page and drop the renamed files into Neutral Face Emoji Tools' uploader.

## Authors

[Dan Chiniara](https://github.com/djchinia)

## Acknowledgments

* Inspiration: https://gist.github.com/lmarkus/8722f56baf8c47045621 
* Renaming Files: https://www.geeksforgeeks.org/rename-multiple-files-using-python/ 

