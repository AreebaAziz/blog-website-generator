# PR - Issue Management System using Solid

Hey all! 

I created an Issue Management app using Solid. Please check it out here and let me know if you find bugs/have any feedback! 

I know that GitHub's issue management system (along with others like Atlaissain, Trello etc) are very sufficient and don't need replacement, and companies probably are ok with storing their data on these servers, but I simply just chose this as a way for me to experiment with Solid and try out a concept (explained below) in practice. I checked what Solid apps are currently in development and didn't find any for issue management so this was a good option for me.

I had this vague idea for about a year - to let users control where to store their data for an app, as well as control the UI. I wanted them to be able to fully customize their own app experience, and be able to add full-stack plugins to the app to enance functionality. I wanted these plugins to easily be able to be installed just by finding the plugin in some app/plugins store and clicking Install, as you do with App Stores/browser plugin stores. 

The end result I implemented is this:
- starting point: users who wish to set up an Issue Management app can do so by:
	- choosing a compute instance to install the backend app to, or choosing the centralized compute servers currently provided by me.
		- The compute instance must have the required hardware/OS specs as required by the backend app program. For this app, it requires an Ubuntu 20 host running on an x86 processor. (Another possible idea is bundling the backend app as a node program, so the program can be installed as an AWS Lambda which is much easier than provisioning and maintaining a compute instance)
		- The compute instance must meet the networking requirements. For this app, the server needs to be available on a predefined HTTP URL (that you define when configuring the app) on port 80. (Can define detailed networking configuration requirements such as protocols, ports, ingress/outgress etc)
	- Setting up a URL to access the backend server by. Can either use an IP address that goes directly to your compute instance, or set up a domain/sub-domain. (Think about: do we want to own a domain where users can easily automatically request a sub-domain?)
	- Setting up a CDN to distribute frontend assets 
	- Setting up a repository to store frontend assets + code / plugins. During this setup, must set the URL for the backend server (so the frontend knows which backend URL to call). (Think about: CORS?)
	- Setting up a URL/domain to access the frontend
- At this point their app instance should now be accessible through their frontend URL, and be fully functional with the backend.

Next, if a user wishes to add functionality to their app instance, such as, for example, the feature to add comments to an issue, they can do so by following these steps:

- search for the IssueMgmnt-Comments plugin on the Plugins Store (currently the plugins are just stored on this GitHub file)
- Install the plugin (backend)
	- This plugin contains the backend plugin to add to the backend server program. Currently I've implemented the backend using Node, so the backend component of the plugin is available as an npm package.
	- Deployment should be as automated and simple as possible. For eg. maybe there is a UI for the Plugins store page, and when installing, you enter the URL of the compute instance. Maybe this compute instance is also running a worker that will process plugin deployments. Or, maybe there is an automated program (like another Lambda) that will re-install the app Lambda and include the new plugin npm package. 
- Install the plugin (frontend)
	- Again, deployment should be as automated and simple as possible. Maybe there's a worker/agent that updates your instance of the frontend repo with the new repo including the frontend package code. 
- At this point, if all works, then now you should be able to see the Comments section on an Issue on your version of the app. This should work with the backend and frontend. 

Now all this is great, but what if you have preferences on the style of the UI of a plugin? Then perhaps the plugin can provide a preferences menu on the UI, or, you can install a frontend-only UI-plugin that works with the backend/interface/API of the IssueMgmnt-Comments plugin. This way, with the same backend logic and API, you can plug your own preferred UI over it. Or you can develop your own as long as you implement the required API of the backend feature plugin! :) 


Anyway, I hope you can get the chance to play around with this. Please do let me know your feedback and/or critism. My ultimate goal is to build on this further, make this idea more robust etc, so that anyone can create any apps in this way, and ultimately end-users will have full control of their entire app experience - from the way it looks/behaves on the frontend, to how it is stored in the backend. Something I was thinking about is whether we want to make the business-logic/core backend of an app replaceable. But, if every component of an app is replaceable, what defines an app? Maybe in the long run there can be lots of options of frontends/backends/core business-logic/feature plugins available, so users can easily put together their own creative versions of an app. They can even create 2 different versions of an Issue Management app, each with their own combinations of plugins! Not sure though, do let me know what you think, and if all this even makes sense... 

Thanks for reading! 







