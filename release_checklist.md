Source

10 Questions to Ask Before You Release To Production – Software Management Blog
Below are the top 10 questions I try to ensure I have answered before we release a new feature into production.

1. **What is the release strategy?**  
Here are 3 options: 
    * **Big Bang** – This is the simplest form of release, where you roll out the feature to your entire user base.  This can either be done with a Feature Gate (or switch), or via the deployment itself.
    * **Incremental** – This is where you initially roll out the feature to a small subset of users.  You may choose to roll it out to a specific region, user role, or other demographic.  Once you have some confidence after the initial rollout, you increase the user base (at whatever rate you desire) until it eventually gets to 100%.
    * **Parallel** – This one isn't always an option, but it's great to use when possible.  Let's say you are making some performance improvements to a complex DB query.  Rather than using the big bang and incremental approaches described above, or implementing some crazy regression testing strategy, you can use the parallel live technique.  With this approach, you run the query simultaneously through the legacy and new code paths.  If the results are the same you just return them.  If they are different you return the legacy result to the user and log the difference for review later.  This approach allows you to test out complex refactoring's with no risk to your users.
2. **What about feature gating (a.k.a. feature flags or dark launch)?**  How will the feature be enabled in production?  Can it be turned on for additional users without a redeploy?  Check out this Forbes article [HERE][1] for some more info on how Google and Facebook leverage feature gating.  Another interesting article from HBR on feature gating [HERE][2].
3. **What is the rollback plan?**  What happens if this feature causes issues in production?  Can it be disabled with a feature switch?  Or is another deployment necessary?  If so, what's the estimated downtime?  How will we know if there is an issue?  Will an alarm go off or do we need to manually test?
4. **Was the code peer reviewed?  **This one might sound like a no-brainer to some, but you'd be surprised how many companies still don't perform peer reviews.  If you aren't using [github][3] which has reviews built right into their pull request mechanism, there are still countless other tools out there that make peer reviews painless.  One I've seen used successfully in the past is [Code Collaborator][4].  Also, it's a good idea to rotate the reviewers or spot check them, as some developers will treat them with a rubber stamp.
5. **Did you write any unit tests?  **If you are writing a new feature, you should add in unit tests where possible.  If you are making tweaks or refactoring an existing feature it would be great to add in some tests now while you have spent the time to grok this section of the code base.
6. **Was any load testing performed?  **Besides standalone load tests (e.g. [JM][5][eter][5], and many others), another great technique to use is HTTP replay, where you replay your production traffic through a staging environment.  We've seen countless times where our canned JMeter tests didn't catch all the corner cases that a production user's data could.
7. **Did QA approve the feature?**  Ideally the answer to this question is automated by using some project tracking tool like [JIRA][6].
8. **Did the PO (product owner) and UI/UX review the implementation?  **I can't tell you how many times I've seen a seemingly simple feature get misinterpreted between the various stakeholders, including product owner, UI/UX, customer, and engineer.  It's a great idea to just pull this folks over to your desk for a quick review of what is being rolled out.
9. **What about DevOps?**  Is any new infrastructure necessary for the release?  Are there any release timing dependencies?  What about config settings?
10. **Do we need to communicate release notes to customers?**  In many companies communication with the customer is handled by product mgmt.  However, if you're in a startup you may need to handle this one yourself.
 

That’s it!  I try to make sure I have a good idea of the answers to these questions for all new features that get rolled out.  Unfortunately sometimes things slip through the cracks.  However, I’ve noticed that most issues that arise downstream could have been avoided by first getting answers to the questions above before you ship.

EDIT:  I recently created a Production Readiness Checklist that condenses this blog post into a single, good looking sheet of paper that you can pass out to your team or hang on the wall in the office.  You can get a copy of this checklist by signing up for our mailing list on the right!

- https://softwareengineering.stackexchange.com/questions/109249/general-checklist-before-releasing-software

These are the items that I've come up with so far:

Is code commented appropriately?
- Does the code adhere to the defined Company Standards?
- Is there error handling in place?
- Is there appropriate security?
- Is there appropriate logging?
- Is localisation required?
- Have release notes and any accompanying documentation been produced?
- Has all testing and debugging code been removed?
- Has sensitive data been such as passwords and licence keys been removed?
- Has performance been checked? Any memory leaks?
 
Maybe you want to consider this:

- What security privs are required to install the software?

- Is the installation drive independent?

- Does the install process test for space availability?

- Is the connection string to the database automatically built or statically coded and requires user change?

- Does your code handle dialect specific data such as date correctly?

- Would your security use MS Windows security? Did you test that?

- What are the other software dependencies assumed at the target client machine (such as .NET Framework, ODBC, OLEDB, etc.) - Does your installation take care of this?

- Does the install script have an un-install that safely removes the software?

- If your software alters the registry during install, do you make a backup of the registry before altering it?

- Does your software expect the certain ports to be open on the firewall so that it runs? Do you check for this?

- If your software is browser based, do you tell the user about supported browsers?

- If your software is windows based, do you tell the user about the windows resolution you see best (unless the application supports all resolutions)?

- Sometimes, compliance with handicapped users may be required.

- Do your user have means to contact you when things don't work as expected?

- Do you have license agreement in place. Does the install process takes that in consideration

- Have you checked all due copyrights?

- Did you confirm that the licensing mechanism (generating userid/password) work?- 

- Is there a generated change log?
- Is everything checked into the VCS?
- Have we added and successfully run tests for each bug discovered in the previous release?
- Has anybody deployed it on a running system?
- Has anybody used it to do something non-trivial?
- Is there a working downgrade procedure?
- Does the package update user editable files (such as configuration) gracefully?
- Do all the unit tests pass?
- Has the software been tested on a preproduction environment / on all the supported OSes?
- Has the software been tested by non-technical people? Any usability issues?
