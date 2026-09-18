# Task 6: Verify the AI Receptionist \[10 minutes\] { #task-6-verify-the-ai-receptionist-10-minutes }

You will now test the AI Receptionist you built, by calling the assigned number and interacting with it using natural language.

- We assigned a PSTN number, the <strong>External Caller number</strong> in the <em>Lab\_Info.txt</em> file on <strong>Workstation 1’s desktop</strong>, to the <strong>AI Receptionist</strong>.


- You can call the AI Receptionist using this PSTN number from your mobile phone.

    - Alternatively, you can log into the Webex App on your laptop or mobile phone as Charles Holland and dial the extension “<strong>6023</strong>”.

- Reference the table below for information on users, workstations and numbers to use.


- User ID and password can be found in [Task 1: Step 3 – Login Credentials for Control Hub and Webex App](01-access-the-lab.md#step-3-login-credential-for-control-hub-and-webex-app).

| User | Number / Ext | Role | Workstation to use |
| --- | --- | --- | --- |
| Charles Holland | - / 6018 | Caller / Customer | Your laptop or mobile phone |
| AI Receptionist | External Caller # / 6023 | Interactive Agent | Call from PSTN (mobile phone) or Charles Holland (Webex App) |
| Anita Perez | - / 6017 | Operator / Human Agent | Not log into Webex App – call sent to her Voicemail<br>Logged into Webex App – call sent to her Webex App |

## Step 1: Call AI Receptionist { #step-1-call-ai-receptionist }

Recommend using your mobile phone and calling the AI Receptionist PSTN number that you configured for it.

Alternatively, you can call from <strong>Charles Holland’s</strong> Webex App, that is logged into your laptop or mobile phone, by dialing ‘<em>x6023</em>’.

1. Call the AI Receptionist:

    - Dial the assigned PSTN number from your mobile phone

<strong>-- OR --</strong>

- Dial ‘<em>6023</em>’ from Charles Holland’s Webex App

2. When the AI Receptionist answers the call, ask some questions that you have configured for its Knowledge Base.

Here are some example questions you can use:

- What are your hours?


- What is your address?


- Do you have warranties?

3. Try asking if you can schedule an appointment or talk to someone about warranties? The AI Receptionist should transfer the call to Anita Perez at x6017.

- If you are still logged into the <strong>Webex App</strong> as <strong>Anita</strong> on <strong>Workstation 2</strong>, you will hear and see the incoming call and can answer it.


- If you are not logged into the <strong>Webex App</strong> as <strong>Anita</strong> on <strong>Workstation 2</strong>, you will hear the call transferred to Anita Perez’s Voicemail box.

4. Now let’s try one of the intent-based transfers by asking the AI Receptionist a question around Webex Contact Center support or configuration.

Repeat step 1 and call back into the AI Receptionist. Now ask one of the following questions:

- I need help with configuring Webex Contact Center?


- I’m having issues configuring a Webex Contact Center supervisor and need help?

5. This time the call should be routed to the Webex Contact Center Customer Assist Support queue. This is based on the intent you configured to route calls to this resource for any topics related to Webex Contact Center.

- If you are logged into the <strong>Webex App</strong> as <strong>Taylor</strong> on <strong>Workstation 4</strong> and <strong>Taylor</strong> is set to <strong>Available</strong>, the call will be forwarded from the queue to Taylor and you will see the incoming call. You can answer or decline the call.


- If you are not logged into the <strong>Webex App</strong> as <strong>Taylor</strong> on <strong>Workstation 4</strong> or <strong>Taylor</strong> is set to <strong>Unavailable</strong>, the call will wait in the queue for an available agent.

6. If you answered the call, hang up.

For now, close the browser window that opens when you answered the call. We will discuss this later in the lab.

**You have completed Task 6 and the lab guide.**
