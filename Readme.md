# Installation
Download the workspace and run `gw initBundle`.

# How to Run
1. After writing your CX code in your CX classes, start your Liferay bundle.
2. Run `./restart.sh` in the Node.js app (please use node 18 ->nvm use v18.14.2) .
3. For the Java app, run `gw clean && gw deploy && gw bootRun`.

# How to Test
1. Create an object called `log` with two text fields: `datetime` and `message`.
2. Go to the user object and configure an action to trigger our CX "on updating" the user object.

