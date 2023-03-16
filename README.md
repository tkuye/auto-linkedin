# Auto-LinkedIn How To Guide

## **Requirements**

1. Must have `Python 3.8` or higher installed on your computer. For tips on how to install `Python` , visit the following resources:
    1. For MacOS
        1. [https://www.dataquest.io/blog/installing-python-on-mac/](https://www.dataquest.io/blog/installing-python-on-mac/)
    2. For Windows
        1. [https://www.tomshardware.com/how-to/install-python-on-windows-10-and-11](https://www.tomshardware.com/how-to/install-python-on-windows-10-and-11)
2. Must have `git` installed on your computer. For tips on how to install `git` visit:
    1. [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## **Downloading the Repository**

Run the following in the terminal on Mac or the CMD on Windows:

```bash
git clone https://github.com/tkuye/auto-linkedin.git
```

This will create a new folder on your computer named `auto-linkedin`.

To enter this new folder, use the following command:

```bash
cd auto-linkedin
```

You then need to run the following:

```bash
pip install -r requirements.txt
```

## **Getting Login Identities**

You will need login identities in order to access and send out connection requests. Visit the guide on how to create a new identity to learn more. These are a few default identities you can use. 

### What is an identity?

An identity is simply the logged in user for a LinkedIn account. By having access to a given identity, you can send out connections and additionally find new leads.

### How do I get the default identities?

Go to the following link and download it to your computer.

[https://drive.google.com/drive/folders/19KOSyj2oZKIXXHrIg2op2x-Vk-KitCHP?usp=share_link](https://drive.google.com/drive/folders/19KOSyj2oZKIXXHrIg2op2x-Vk-KitCHP?usp=share_link)

**Move the downloaded login identities folder to `auto-linkedin` folder.**

Drag and drop the newly downloaded identities folder into the `auto-linkedin` folder.

## Finding Leads with Recruiter Lite

This guide outlines how to get the leads for a given keyword, downloaded to your computer.

1. To get the URL, first log into the account with access to Recruiter Lite.
2. Once you have logged in, navigate to Recruiter Lite.
3. Click on **Start new Recruiter search**
    
    [Image of Starting a Recruiter Search](https://lh5.googleusercontent.com/R4OIoHGuVDGDF6fatn3uwSyXlmkqUHt_F4UAB3ndbtbJtmemh863eh10ilcaTnxWrApcKpgOipo2bj1ZKVouMka7uNp6EqiZ3pXMGH70qaQ4eNIBWA4jp-8MdC4-ro8-Hy4aMy1UjaAs02JjHY0PCOo)
    
    Image of Starting a Recruiter Search
    
4. Add the **selected keyword** filters to the search.
    
    [Image of a sample recruiter search with keywords.](https://lh4.googleusercontent.com/J73aU7Idv-z5f8Ym0qhvDh-K5JFFViAls-ga-Y_4JR20Uhix-WTzWO7ZW4vwEmlf7F5cezVVFpM6Nq-hOzs3VqUGTKfDoPnRdcZX1fhqBiNbMg1pSBWF_b1qLbPlSr6PewVBUJU4WuxmXvnnIcktasE)
    
    Image of a sample recruiter search with keywords.
    
5. Press enter to make the search. Once the search has been created, you want to use your keyboard and type **CMD Option I** on Mac or **CTRL Shift I** on Windows to open the inspect element pane. Should look like the image below.
    
    [Image of screen with Inspect Element Tab open.](https://lh3.googleusercontent.com/9qnQ54L8V2KlrgKD_1mR-l8G1aAvuiGe8AaSCY4NXn_iBoUJeOnX4YgeIxS1pnP8uXeqKNci2rIirGD5ooL-w4mgy6Tm4aKaVB3jrQ_g84mJjiKSJOCt2cxrxPEHQEbv4JYsaRJjDbbZH5Z26cZg2f4)
    
    Image of screen with Inspect Element Tab open.
    
6. Within the Inspect Element Pane, navigate to the ***Network*** Tab.
    
    **On Chrome:**
    
    [https://lh3.googleusercontent.com/mhp_6pU32n-hzop5wN8-qvK47sqgvu6P6VuS-HqKELpXSbX4dNOHmaLvqqLWvmYiaAS9NvqwayQJb-JcpRYWpT0JE2PhVtOkPGEwLRrsW9hNO4ZHzDLON7VdE0j3SVBmz__J2zjtDN4-GH66Tx9fRtI](https://lh3.googleusercontent.com/mhp_6pU32n-hzop5wN8-qvK47sqgvu6P6VuS-HqKELpXSbX4dNOHmaLvqqLWvmYiaAS9NvqwayQJb-JcpRYWpT0JE2PhVtOkPGEwLRrsW9hNO4ZHzDLON7VdE0j3SVBmz__J2zjtDN4-GH66Tx9fRtI)
    
    **On Safari:**
    
    [https://lh3.googleusercontent.com/8qntve6t3yPz6GkX2lY5LtlnYXTxroQK6Q277gfxYC7Os_fuuFVpzMc6p8r-GzqO5Boh4cLR5l_hDO74Bp60p0eOWZYTJfUeNkJ4_ZsqNMIt7ameXBSvaVTk1TdxIdmc1aFeFWlhjOxCdWAA5M78YUk](https://lh3.googleusercontent.com/8qntve6t3yPz6GkX2lY5LtlnYXTxroQK6Q277gfxYC7Os_fuuFVpzMc6p8r-GzqO5Boh4cLR5l_hDO74Bp60p0eOWZYTJfUeNkJ4_ZsqNMIt7ameXBSvaVTk1TdxIdmc1aFeFWlhjOxCdWAA5M78YUk)
    
7. Refresh the page to see the new network requests. Should look as follows:
    
    [https://lh5.googleusercontent.com/WFLniRYdtsSMY8FgGzR0ZwrsRyRpa-7efwIPno2kwhEnUGD4oRT7toCVn6GCYk78MF_OKETijKbjiP3zYXm_cFOU1rdBaPU_gSxwMMcKKlh5IKv-cJuEjxiYuPUGxExUhqwZrPsqfs8I2YMT32tCq0Y](https://lh5.googleusercontent.com/WFLniRYdtsSMY8FgGzR0ZwrsRyRpa-7efwIPno2kwhEnUGD4oRT7toCVn6GCYk78MF_OKETijKbjiP3zYXm_cFOU1rdBaPU_gSxwMMcKKlh5IKv-cJuEjxiYuPUGxExUhqwZrPsqfs8I2YMT32tCq0Y)
    
8. Look for the network request from the list with the name: **talentRecruiterSearchHits**
    
    [https://lh3.googleusercontent.com/jVnXCgbgU-jspVS4L21lLTab0HcURHDGkqD4tQzUkmNPvn28qJNnPUFatxeSEmb1Xn2z-TaipabVfHBXe4nCNG3JXyUIFQf6W0cRTRBYKmkDWba6XXTpa5D-NSoJkfHrncPsmjSQIJkspzUPaySJvDI](https://lh3.googleusercontent.com/jVnXCgbgU-jspVS4L21lLTab0HcURHDGkqD4tQzUkmNPvn28qJNnPUFatxeSEmb1Xn2z-TaipabVfHBXe4nCNG3JXyUIFQf6W0cRTRBYKmkDWba6XXTpa5D-NSoJkfHrncPsmjSQIJkspzUPaySJvDI)
    
9. Once found, **Right** **Click** on it, and a menu should appear. From this menu, click **Copy Link**.
10. Go back to the `auto-linkedin` folder and enter the folder named scripts. Within this folder, there are three subfolders named: **`windows`, `linux`** and **`mac`.** Choose the folder corresponding to your computer, and click on the file named `find_recruiter`.
11. Once the file is open, it should look like this on `mac` or `linux`:
    
    ```bash
    #!/bin/sh
    
    python3 -m src.recruiter find \
    --url 'https://www.linkedin.com/talent/search/api/talentRecruiterSearchHits?decoration=%28entityUrn%2ClinkedInMemberProfileUrn~%28entityUrn%2CreferenceUrn%2Canonymized%2CunobfuscatedFirstName%2CunobfuscatedLastName%2CmemberPreferences%28openToNewOpportunities%2CproxyPhoneNumberAvailability%29%2CcanSendInMail%2CcontactInfo%28primaryEmail%29%2CcurrentPositions*%28company~%2CcompanyName%2Ctitle%2CstartDateOn%2CendDateOn%2Cdescription%2Clocation%29%2Ceducations*%28school~%28entityUrn%2Cname%29%2CorganizationUrn~%2CschoolName%2CdegreeName%2CstartDateOn%2CendDateOn%29%2CfirstName%2CfullProfileNotVisible%2CfullProfileNotVisibleReason%2Cheadline%2CindustryName%2ClastName%2Clocation%28displayName%29%2CnetworkDistance%2CnumConnections%2CprivacySettings%28allowConnectionsBrowse%2CshowPremiumSubscriberIcon%29%2CprofilePicture%2CpublicProfileUrl%2Cunlinked%2CvectorProfilePicture%2CworkExperience*%28company~%28entityUrn%2Cindustries%2Cname%29%2CcompanyName%2Ctitle%2CstartDateOn%2CendDateOn%29%29%2CrecruitingProfile~%28entityUrn%2Ccandidate%2CcurrentHiringProjectCandidate%28created%2ClastModified%2CentityUrn%2ChiringProject~%28entityUrn%29%2CcandidateHiringState~%2CsourcingChannel~%28entityUrn%2CchannelType%29%29%2ChiddenCandidate%2ChiringContext%2Cnotes*%28candidate%2CchildNotes*%28candidate%2CchildNotes*%2Ccontent%2Ccreated%2CentityUrn%2ChiringContext%2ClastModified%2Cowner~%28entityUrn%2Cprofile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2Cproject%2CmessageModified%2Cmessage%2CparentNote%2Cvisibility%2CsourceType%29%2Ccontent%2Ccreated%2CentityUrn%2ChiringContext%2ClastModified%2Cowner~%28entityUrn%2Cprofile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2Cproject%2CmessageModified%2Cmessage%2CparentNote%2Cvisibility%2CsourceType%29%2CprofileUrl%2Cprospect%2Ctags*%29%2ChiringProjectRecruitingProfile~%3AhiringProjectRecruitingProfile%28entityUrn%2CassessedCandidate%28rejectable%29%2Ccandidate%2CcurrentHiringProjectCandidate%28entityUrn%2Ccreated%2ClastModified%2CaddedToPipeline%28time%2Cactor~%28profile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%29%2ChiringProject~%28entityUrn%2ChiringProjectMetadata%28hiringPipelineEnabled%2Cstate%29%29%2CcandidateHiringState~%2CsourcingChannel~%28entityUrn%2CchannelType%29%29%2ChiddenCandidate%2ChiringContext%2ClastActivity~%28activityType%2Cperformed%28time%2Cactor~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2CperformedByViewer%2ChiringActivityData%29%2CsourcingChannel%2CsourcingChannelCandidates*%2CassessmentCandidateQualificationResponses*%28assessmentQualificationUrn%2CrecruiterReplyDueAt%2CresponseSubmittedAt%29%2CcandidateInsights%28candidateHiringProjectInsightsUrn~%28candidateSimilarity%2CentityUrn%29%29%2C~hiringProjectCandidatesCount%28paging%29%29%2CcandidateInsights%28candidateSearchInsightsUrn~%28positionsInsight%2CyearsOfExperience%2CentityUrn%29%29%29&count=25&q=recruiterSearch&query=(capSearchSortBy:RELEVANCE,facets:List(TALENT_POOL))&requestParams=(searchContextId:9066a300-7f10-4188-b020-bfeb85d5e24e,searchRequestId:d93cb936-7b7b-42e6-8b38-277e243cd11f,searchHistoryId:5432231506,doFacetCounting:true,doFacetDecoration:true,uiOrigin:FACET_SEARCH,reset:List(),resetProfileCustomFields:List())&start=0' \
    --identity identities/appleseed \
    --output data/recruiter/leads/ualberta_2025_2026.json \
    --start 0 \
    --count 25 \
    --end 100
    ```
    
12. You want to edit the line that has `--url` with the url you previously copied from the Inspect Element page.
13. Next, you want to make sure the `--identity` is directed to the folder with the name of the account with access to Recruiter Lite. In this case it should be `identites/appleseed`. 
14. Then, you want to set the location of where you want the new leads that are collected with the `--output` command. This can be any location on your computer, but try to keep it consistent as you will need this later. 
15. Once you have edited the `--url` , `—identity` and `—output`  save the file. 
16. The process is very similar on Windows, except your file will look like this:
    
    ```powershell
    @echo off
    
    python3 "-m" "src.recruiter" "find" "--url" "https://www.linkedin.com/talent/search/api/talentRecruiterSearchHits?decoration=%28entityUrn%2ClinkedInMemberProfileUrn~%28entityUrn%2CreferenceUrn%2Canonymized%2CunobfuscatedFirstName%2CunobfuscatedLastName%2CmemberPreferences%28openToNewOpportunities%2CproxyPhoneNumberAvailability%29%2CcanSendInMail%2CcontactInfo%28primaryEmail%29%2CcurrentPositions*%28company~%2CcompanyName%2Ctitle%2CstartDateOn%2CendDateOn%2Cdescription%2Clocation%29%2Ceducations*%28school~%28entityUrn%2Cname%29%2CorganizationUrn~%2CschoolName%2CdegreeName%2CstartDateOn%2CendDateOn%29%2CfirstName%2CfullProfileNotVisible%2CfullProfileNotVisibleReason%2Cheadline%2CindustryName%2ClastName%2Clocation%28displayName%29%2CnetworkDistance%2CnumConnections%2CprivacySettings%28allowConnectionsBrowse%2CshowPremiumSubscriberIcon%29%2CprofilePicture%2CpublicProfileUrl%2Cunlinked%2CvectorProfilePicture%2CworkExperience*%28company~%28entityUrn%2Cindustries%2Cname%29%2CcompanyName%2Ctitle%2CstartDateOn%2CendDateOn%29%29%2CrecruitingProfile~%28entityUrn%2Ccandidate%2CcurrentHiringProjectCandidate%28created%2ClastModified%2CentityUrn%2ChiringProject~%28entityUrn%29%2CcandidateHiringState~%2CsourcingChannel~%28entityUrn%2CchannelType%29%29%2ChiddenCandidate%2ChiringContext%2Cnotes*%28candidate%2CchildNotes*%28candidate%2CchildNotes*%2Ccontent%2Ccreated%2CentityUrn%2ChiringContext%2ClastModified%2Cowner~%28entityUrn%2Cprofile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2Cproject%2CmessageModified%2Cmessage%2CparentNote%2Cvisibility%2CsourceType%29%2Ccontent%2Ccreated%2CentityUrn%2ChiringContext%2ClastModified%2Cowner~%28entityUrn%2Cprofile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2Cproject%2CmessageModified%2Cmessage%2CparentNote%2Cvisibility%2CsourceType%29%2CprofileUrl%2Cprospect%2Ctags*%29%2ChiringProjectRecruitingProfile~%3AhiringProjectRecruitingProfile%28entityUrn%2CassessedCandidate%28rejectable%29%2Ccandidate%2CcurrentHiringProjectCandidate%28entityUrn%2Ccreated%2ClastModified%2CaddedToPipeline%28time%2Cactor~%28profile~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%29%2ChiringProject~%28entityUrn%2ChiringProjectMetadata%28hiringPipelineEnabled%2Cstate%29%29%2CcandidateHiringState~%2CsourcingChannel~%28entityUrn%2CchannelType%29%29%2ChiddenCandidate%2ChiringContext%2ClastActivity~%28activityType%2Cperformed%28time%2Cactor~%28entityUrn%2CfirstName%2ClastName%2Cheadline%2CprofilePicture%2CvectorProfilePicture%2CpublicProfileUrl%2CfollowerCount%2CnetworkDistance%2CautomatedActionProfile%29%29%2CperformedByViewer%2ChiringActivityData%29%2CsourcingChannel%2CsourcingChannelCandidates*%2CassessmentCandidateQualificationResponses*%28assessmentQualificationUrn%2CrecruiterReplyDueAt%2CresponseSubmittedAt%29%2CcandidateInsights%28candidateHiringProjectInsightsUrn~%28candidateSimilarity%2CentityUrn%29%29%2C~hiringProjectCandidatesCount%28paging%29%29%2CcandidateInsights%28candidateSearchInsightsUrn~%28positionsInsight%2CyearsOfExperience%2CentityUrn%29%29%29&count=25&q=recruiterSearch&query=(capSearchSortBy:RELEVANCE,facets:List(TALENT_POOL))&requestParams=(searchContextId:9066a300-7f10-4188-b020-bfeb85d5e24e,searchRequestId:d93cb936-7b7b-42e6-8b38-277e243cd11f,searchHistoryId:5432231506,doFacetCounting:true,doFacetDecoration:true,uiOrigin:FACET_SEARCH,reset:List(),resetProfileCustomFields:List())&start=0" "--identity" "extra_data\identities\appleseed" "--output" "data\recruiter\leads\ualberta_2025_2026.json" "--start" "0" "--count" "25" "--end" "600"
    ```
    
17. You then want to edit the **EXACT** same items in the file: `—-url`, `—-identity` and `—-output` then save.
18. Once this has been saved, you can go ahead and run the following:
    
    ```bash
    ./scripts/mac/find_recruiter.sh
    ```
    
    ```bash
    ./scripts/linux/find_recruiter.sh
    ```
    
    ```bash
    scripts\windows\find_recruiter.bat
    ```
    
19. This should then start running the script and save the found leads to the file specified by the `--output` command. 
20. That’s it! You’re ready to start sending connections. 

## Sending Connections from Recruiter Lite Leads

This is a guide on how to send out leads from a given identity using data retrieved from Recruiter Lite. If you haven’t already gone through the guide on how to get the leads, visit that above first. 

1. Head into the `scripts` folder and find the file named `recruiter.sh` or `recruiter.bat` depending on your computer type. (One of `windows` `mac` or `linux`).
2. Open the file and you should see something like this: 
    
    ```bash
    #!/bin/sh
    
    python3 -m src.recruiter connect \
    --leads data/recruiter/leads/sample.json \
    --identity identities/john \
    --max_connections 50 \
    --message data/messages/business_development.txt \
    --send_delay_min 60 \
    --send_delay_max 120 \
    --person John \
    --connect_file data/recruiter/connections/sample.csv
    ```
    
    ```powershell
    @echo off
    
    python3 "-m" "src.recruiter" "connect" "--leads" "data\recruiter\leads\sample.json" "--identity" "identities\john" "--max_connections" "50" "--message" "data\messages\business_development.txt" "--send_delay_min" "60" "--send_delay_max" "120" "--person" "John" "--connect_file" "data\recruiter\connections\sample.csv"
    ```
    
3. This outlines each of the given arguments within the file:
    - `--leads` The file associated with the data collected from Recruiter Lite.
    - `--identity` This is the identity or profile you want to send the connections from.
    - `--max_connections` This is the maximum number of connections you want to send from that account in this script.
    - `--message` This is the path to the file with the message you want to send to the candidate. This message should have the following structure with the `{name}` field and `{person}` field which will be dynamically changed.
        
        ```
        Hey {name}, I’m {person} and my startup LocalStudent is currently hiring Business Development Associates. I came across your profile and I’m really impressed with your experiences! Are you currently looking for a Summer 2023 position or a part time position this winter?
        ```
        
    - `--send_delay_min` The minimum delay time in seconds to send the next connection request.
    - `--send_delay_max` The maximum delay time in seconds to send the connection request.
        - **NOTE:** All the connection requests are sent randomly, so the true delay will be a number between the `--send_delay_min` and `--send_delay_max`.
    - `--person` This is the name of the person you want used in the message to fill the `{person}` field. This ideally should be the same name as the identity folder.
    - `--connect_file` This is the name of the file you want to save the connections whether successful or failed to. Specify the path or location you want to use. This is saved as a `csv` file, so you can quickly add the data to an Excel Spreadsheet or Google Sheets.
4. Edit the arguments that are necessary to you. For example, if you want to send out connection requests from **Susan’s** LinkedIn account every **3-5** minutes for a maximum of **30** requests, the file would like the following:
    
    ```bash
    #!/bin/sh
    
    python3 -m src.recruiter connect \
    --leads data/recruiter/leads/susan_sample.json \
    --identity identities/susan \
    --max_connections 30 \
    --message business_development.txt \
    --send_delay_min 180 \
    --send_delay_max 300 \
    --person Susan \
    --connect_file data/recruiter/connections/susan_sample.csv
    ```
    
    ```powershell
    @echo off
    
    python3 "-m" "src.recruiter" "connect" "--leads" "data\recruiter\leads\susan_sample.json" "--identity" "identities\susan" "--max_connections" "30" "--message" "business_development.txt" "--send_delay_min" "180" "--send_delay_max" "300" "--person" "Susan" "--connect_file" "susan_sample.csv"
    ```
    
5. Once, you have made the appropriate edits to the following `recruiter` file. You can run it like so:
    
    ```powershell
    ./scripts/mac/recruiter.sh
    ```
    
    ```powershell
    ./scripts/windows/recruiter.bat
    ```
    
    ```powershell
    scripts\linux\recruiter.sh
    ```
    
6. Once, the script is running, simply wait until it’s complete! Depending on the delay you set between each request and the number of requests total, it may take anywhere from 10 minutes to 2 hours (or longer).
7. Congrats, you’ve reached the end of this guide!

## Running All Scripts in Folder

This is a guide to run all files in a given folder as one command. 

1. To begin, we need to find the `exec.sh` file. This file will be located in the `scripts` directory underneath the type of computer available. Once you have located the file, click on it to edit. 
2. The file should look something like this on MacOS or Linux:
    
    ```bash
    #!/bin/sh
    
    python3 -m src.exec --directory \
        scripts/test # edit this line to run a different script with a different folder.
    ```
    
    On Windows:
    
    ```visual-basic
    @echo off
    
    python3 "-m" "src.exec" "--directory" "scripts\test" REM Edit the script\test directory to point to your directory.
    ```
    
3. Next, you want to edit the value beside or below the `--directory` argument. This will be the path to the folder you want all the files ran in. After changing this value to any folder, save the file. 
4. You can now run the script with the following commands:
    
    ```bash
    ./scripts/mac/exec.sh
    ```
    
    ```bash
    ./scripts/linux/exec.sh
    ```
    
    ```bash
    scripts\windows\exec.bat
    ```
    

## Scheduling Scripts

This is a guide on how to schedule a given script to be run daily, weekly or monthly. In this case we will focus on it being run daily at 9AM every day. 

**********NOTE: THIS ONLY WORKS FOR MAC AND LINUX COMPUTERS**********

To run a script daily we will have to make use of a program known as `crontab.` `crontab` helps you run programs by specify the information associated with when the script should run. 

For our use case, we will be specifying the `scripts/mac/exec.sh` file to be run everyday at 9 AM. 

1. We need the path of our file. We have two options. 
    1. Using the Finder display on Mac, find the file then **Right Click** on it. You will see a dropdown option named **Get Info.** Click on this to see the absolute path of the file. 
    2. Using the terminal, navigate to the location of the `exec.sh` file using the `cd` command. Once you are in the correct directory, type the following:
        
        ```powershell
        pwd
        ```
        
        This command will show the current path of the file. Copy this value. You should see something like this:
        
        ```powershell
        /Users/username/Desktop/project/scripts/mac
        ```
        
2. Next, we want to schedule this script. To schedule it to run daily, enter the terminal and enter the following:
    
    ```powershell
    nano crontab -e
    ```
    
    This should open up a file. In this file, paste the following, but change the path to the script that you previously got in step 1. 
    
    ```powershell
    0 9 * * * /Users/username/Desktop/project/scripts/mac/exec.sh
    ```
    
3. You can then run CTRL- S to save the file, and that’s it! The script is now scheduled to run at **9 AM** everyday. To stop running the script. Go through step 2 again, but delete the content of the file and save it.