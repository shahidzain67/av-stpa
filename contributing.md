Title: Contributing
URL:
save_as: contributing.html

# Contributing

We try to make it as easy as possible to collaborate. The following is a set of guidelines for joining and contributing to the AV STPA project. All of the project documents are hosted under the [Trustable project](https://gitlab.com/trustable/av-stpa) on Gitlab.

Contributions to this project are not limited the STPA itself, but incorporate all parts of the project, including: improvements to how we format / deliver the analysis, improvements to our working processes, and importantly ideas to attract new contributors. It's also important to note that there is no size limit to contributions (it could be as simple as an email pointing out a typo), and joining the mailing list and joining in with discussions does not come with any obligations to contribute to the rest of the work; how much you are involved is entirely up to you.

If you are interested, please join the [Trustable mailing list](https://lists.trustable.io/cgi-bin/mailman/listinfo/trustable-software). This list will contain discussions not just about the AV STPA project but also around trustable software as well.

## How to contribute

There are several ways that you can contribute to the project, including:

* Adding new content / helping with ongoing work
* Reviews and feedback on content, ongoing or past
* Joining in with discussions on the mailing list
* Ideas for improvements

All of the project files are stored on our [Gitlab repo](https://gitlab.com/trustable/av-stpa), however it is not necessary to learn how to use git in order to contribute. If you do not wish to use git, you can start / join in with discussions on the mailing list, and somebody will pick up changes that need to be made as a result of the discussions. Otherwise, see the Gitlab section of this document for instructions.

To discuss this project on the mailing list, please put '[av-stpa]' at the start of the subject.

## Gitlab

We use git, which is a version control system, to control all of the work that we do, and all of the project files are stored on Gitlab. We welcome contributors to interact directly with the project using git. If you are unfamiliar with git, there are plenty of tutorials online. In order to make changes to the project, you will need to:

1. Create a Gitlab account
  - Simply click "sign in/register" in the top right corner on [Gitlab](https://gitlab.com/) and fill in the form.
2. Request developer access to the av-stap repo
  - Go to the AV STPA Gitlab project page and click "Request Developer Access" near the top of the page. One of the maintainers will review the request and grant access.

## Reporting Tasks to be done

All work, whether adding something new or changing something that already exists, should be listed as an **Issue** on the project. The Issues list acts like a TODO list for the project. Contributors are welcome to either add new Issues to the list, or to pick up existing Issues and action them.

This section guides you through submitting an Issue. Before creating an Issue, please check the following:

* Perform a cursory search of the [Issues list](https://gitlab.com/trustable/av-stpa/issues) to see if the problem has already been reported. If it has and the issue is still open, add a comment to the existing issue instead of opening a new one.
* Consider if you can resolve the Issue quickly yourself.

### To submit an Issue on Gitlab:

1. Go to **Issues** (on the left)
2. Click **New Issue** near the top right
3. Fill in the form and click **Submit Issue**, following the guidelines below on how to submit a good Issue.
  - Note when filling in the form you do not have to assign the Issue to anybody, this can be picked up and assigned to somebody later on.

### To submit an Issue via the mailing list

* Your message subject should start with "[av-stpa] New Issue:" followed by the title of your Issue.
* Describe the Issue, in detail, in the message subject, following the guidelines below.

#### How to submit a good Issue

All submitted Issues should be easy to understand, and explain the problem with enough details to help maintainers when they are trying to resolve.

* Use a clear and descriptive title for the issue to identify the problem.
* Describe the problem with more details if necessary in the description section. Sometimes a good title is enough, but as a guide it helps to know:
  - Why are you raising this Issue
  - If known, the steps to resolve the Issue
* Use specifics. If you are talking about something specific, make it clear exactly what you are talking about. "Diagram is wrong" is not very useful, where as "Level 2 control diagram has missing feedback between x and y" is much more helpful.

##  Working on a task

If you want to work on the project, once there is an Issue created for the task that you want to do, that Issue can be assigned to you.

### Working on a task without git

Unfortunately it is harder to work on an Issue without some basic knowledge of git (but not impossible). If there is something that you would like to do, send a message to the mailing list detailing what you would like to do, and a member on the list will assist with what you are trying to do, either helping you to learn the basics of git, or facilitating the git side of things so you can focus on the work.

### Working on a task with git

To work directly on the repo using git, you should do the following:

1. Clone the repo
2. Make a local branch (according to the branching policy described below)
3. Make your changes in the branch
4. Push the branch
5. Open a merge request (the review process is described below)

#### Branching Policy

The main body of work is stored in a branch called **master**. This reflects the most up to date work, and everything in master should have gone through a review process. It is important not to work directly on the master branch, but to create local branches to do your work on.

All work being done should be performed in a unique branch. Branches should be short-lived, and used for a single piece of work or Issue. Once you have finished with the specific thing that you are working on, the branch should be merged to master and then deleted (be careful not to delete a branch until your work is incorporated into master or you run the risk of losing what you have done).

It is recommended that branches have a meaningful name, and the branch name should have your username in the name, as well as the Issue number (if one exists). For example a user called Foo Bar working on Issue 15 should use branch name:

`foobar/15-add-missing-feedback-to-level-2-control-diagram`

Naturally you may create branches which don't end up being merged into master for a number of reasons. Once a branch has no new updates for a period of time, it will be labelled as stale. It is important to review your stale branches and decide whether the work is worth completing and incorporating into master, or deleting if it has become redundant for whatever reason.

#### Review Process

All work to be merged into master will be reviewed and approved. When you open a merge request, you can select who you would like to review and approve your changes. **You should have at least 1 member of the Trustable group review your work**, plus any other specific people that you wish to review. **You cannot approve your own changes.**

Reviewers can open discussions based upon their feedback, and once all discussions have been resolved, the changes will be approved and subsequently merged into master.
