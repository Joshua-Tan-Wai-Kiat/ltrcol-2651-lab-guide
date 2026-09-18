# Content review

## Conversion

The supplied Word guide was converted into an introduction and six task pages.
All 129 embedded image assets were extracted. Word stores both original images
and flattened versions with arrows/callouts; the pages use 76 image occurrences
before public-edition sanitization. The public edition retains 54 reviewed image files and 55 image occurrences; credential-bearing and unused images are excluded. Temporary image extensions were normalized
to PNG or JPEG without recompressing the images.

The 20 Word tables became five data/image tables and 15 note or tip boxes.
The Word table of contents and page numbers were replaced by website navigation.
The general AI Receptionist overview was moved into the introduction. Call-in
options remain with Task 4, as in the source sequence.

Floating Word annotations required special handling to preserve the complete
gateway CLI sequence. Commands, knowledge-base sample content, and receptionist
guidelines are presented as copyable code blocks. The final "proceed to next task"
sentence was changed to indicate completion because the source ends at Task 6.

## Items for the lab owner to verify

The conversion preserves the supplied technical instructions; these issues are
present in the source and are not silently resolved by inventing configuration:

- **Queue setup is assumed.** Tasks 4–6 reference `Q1_WebexCallingSupport`,
  `Q2_WebexContactCenterSupport`, Customer Assist licenses, and agent/supervisor
  assignments. The guide contains no steps to create the queues or assign those
  roles. A prerequisite note was added to the introduction and Task 4.
- **External Caller extension differs.** Task 1 names extension `86023` in
  `Lab_Info.txt`, but its gateway translation rule and the AI Receptionist use
  `6023`. Verify that the leading `8` is expected in the lab numbering plan.
- **Auto Attendant references differ.** The gateway example mentions `7000`,
  while the call-in instructions use `6500`. Verify against the assigned lab.
- **Phone number examples differ.** Task 1 uses `+441189162233`; Task 4 uses
  `+44118916223`. Learners are directed to use their own assigned PSTN number.
- **Credential cross-reference.** Task 2's note refers to "Step 2 above" for
  credentials; Task 1, Steps 2–3 actually contain the session/credential details.
- **Support files are external lab prerequisites.** `APEX UC Solutions-KB.txt`,
  `AI Receptionist Config-KB.txt`, and `AI Receptionist Config.txt` are referenced
  as files on Workstation 1. They were not supplied separately and have not been
  fabricated or added as downloads. The text included in the Word guide remains
  available on the website.
- **Source contains forward references.** Statements about creating queues
  "later" and discussing a browser window "later in the lab" refer to material
  beyond the supplied six tasks.
- **Release-specific content.** The source is dated November 12, 2026 and includes
  a roadmap, language/voice availability, and known knowledge-base upload delays.
  These statements were preserved, not verified as current product behavior.

## Validation scope

Website checks cover the strict MkDocs build, local links and anchors, image
references, all seven page layouts, navigation, search, and screenshot enlargement.
No dCloud, Control Hub, gateway, Webex account, or live calling configuration was
changed or exercised. Lab instructions are content, not actions to execute while
converting the guide.

