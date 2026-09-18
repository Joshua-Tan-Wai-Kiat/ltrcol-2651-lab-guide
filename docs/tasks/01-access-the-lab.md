# Task 1: Accessing the Lab \[10 minutes\] { #task-1-accessing-the-lab-10-minutes }

All components for this lab can be accessed through a web browser or VPN to dCloud

1. Click on the <strong>User Workstation 1</strong> icon on the topology page and it will bring up a fly-out window on left with <strong>Workstation 1</strong> related information. Under <strong>Remote Access</strong> you will see the workstations IP Address, Username, and Password in your assigned session.


2. You can click on any other Virtual Machine on the topology page to get its respective details.

## Step 1: Access the lab { #step-1-access-the-lab }

### Option A: Accessing the Lab with Web RDP/ Remote Desktop \[Preferred\] { #option-a-accessing-the-lab-with-web-rdp-remote-desktop-preferred }

1. With this method, you will use <strong>Workstation 1</strong> as your main access to all the other lab virtual machines or Cisco UC applications needed to complete the lab tasks: Cisco UCM, Unity Connection, Collaboration Control Hub Admin Portal, etc.


2. To access <strong>Workstation 1</strong> over <strong>Web RDP</strong>, click on the <strong>Workstation 1</strong> icon on the topology page and in the fly-out window with workstation 1’s details, expand the ‘<em>Remote Access</em>’ <em>section</em> and click on <em>‘Web RDP</em>’. It will open a new browser tab and connect you to Workstation 1.


### Option B: Accessing the Lab with VPN { #option-b-accessing-the-lab-with-vpn }

1. To connect to <strong>Workstation 1</strong> using your local RDP connection, first, you need to connect to your lab session via VPN. Open the <strong>Cisco AnyConnect</strong> client on your laptop. It will prompt you for the Host Address, username, and password information for your session.


2. You will find all these details on the <strong>Info</strong> page of your lab’s topology page. In the fly-out window expand the ‘<em>Cisco Secure Client Credentials</em>’ section where you will see the <strong>VPN details</strong> of your lab. Enter the details from your assigned session and click “<em>OK</em>” to connect to your session.<br><br><mark>The Host Address, username, and password will be different for each lab. Use <strong>YOUR OWN</strong> assigned lab details.</mark>


3. Once you are connected to your lab session over VPN, you can open a local RDP connection on your laptop and connect to <strong>Workstation 1</strong> using the Remote Access details supplied by your assigned session.


## Step 2: Continuing the lab on User Workstation 1 Desktop { #step-2-continuing-the-lab-on-user-workstation-1-desktop }

On your assigned dCloud session, open **Info** to find the lab domain and assigned PSTN numbers. These are also available in **Lab_Info.txt** or **Session_Info.txt** on Workstation 1. Keep session access information private.

## Step 3: Login Credential for Control Hub and Webex App { #step-3-login-credential-for-control-hub-and-webex-app }

1. On **User Workstation 1**, open **WEBEX_PASSWORD.txt** to obtain the assigned Control Hub administrator account and password.
2. Use the account details supplied with your session for each Webex test user. Consult **Lab_Info.txt** or your lab instructor if a required account is missing.
3. Use these details only in the corresponding lab application's sign-in screen. Do not copy credentials into this public guide.

## Step 4: Update Local Gateway (LGW) Config { #step-4-update-local-gateway-lgw-config }

For this lab you will use 2 PSTN numbers to call in to the Auto Attendant and AI Receptionist. The lab has 1 of these numbers pre-configured so you need to configure the LGW to route the second PSTN number to Webex Calling from the CUBE PSTN gateway.

1. On <strong>Workstation 1’s</strong> desktop, find and open the file “<strong>Lab\_Info.txt</strong>”. This file contains the PSTN numbers assigned to your lab.


2. Find the PSTN number assigned to the <strong>External Caller</strong> and extension <strong>86023</strong>. The PSTN number will be at the end of the line. Use the PSTN number from your own session.


3. On <strong>Workstation 1’s</strong> desktop open Putty from the taskbar


4. In the Putty Configuration window double click on ‘<em>Local Gateway</em>’ under the saved sessions to open an SSH session to the device.


5. Log into the LGW using the gateway credentials provided privately with your assigned lab session.

6. If you type `show run | s voice translation-rule 100000` you will see there is already 1 translation rule for extension 7000.


7. Next you will add a new translation rule for the External Caller extension and phone number you found in step 2 above. Enter the following CLI commands to configure the second translation rule:

    Replace `<YOUR_PSTN_NUMBER>` below (including the leading `+`) with your lab's External Caller PSTN number from step 2.

    ```text
    config t
    voice translation-rule 100000
    rule 2 /6023/ /<YOUR_PSTN_NUMBER>/
    end
    wr mem
    ```


8. To confirm the translation rule has been updated, type `show run | s voice translation-rule 100000` and you should see both the existing rule and the new rule.


9. Type ‘<em>exit’</em> and close the Putty app.

<strong>This task is now completed. Proceed to the next task.</strong>

