# Solid

### Try `solid-flask` Python program to investigate HTTP response from Solid server

##### Nov 16, 2022

First of all, I've already created a few Solid Pods to get started:

My Solid Web IDs:

* https://id.inrupt.com/areeba 
* https://areeba.solidcommunity.net/profile/card#me
* https://areeba.solidweb.org/profile/card#me

The first thing I want to try to do is make a raw HTTP request to my Pod, go through authentication, and access a file from my Pod. 

First I want to see what happens when I make a HTTP GET request to my Pod. 

I want to use Bash commands, and if it gets more complex, Python. But also, I know that they're probably trying to encourage accessing the Pod from JavaScript (frontend directly). So maybe I should use JavaScript. But I wonder in what cases we'd have to have a backend access the data from pods. :thinking:

Found this: 

* https://solidproject.org/developers/tools/
* solid-flask - simple “Hello World” Flask app that can read private data from a Solid pod
* https://gitlab.com/agentydragon/solid-flask/-/blob/master/solid_flask_main.py

##### Nov 18, 2022

Now I will try to download the Python Flask program above and run it using my Inrupt Solid Pod.

```
git clone https://gitlab.com/agentydragon/solid-flask.git solid-flask
```

I opened the folder on VSCode. Now I'm reading the README for instructions. I have to install Bazel. 

* Using Homebrew: https://bazel.build/install/os-x#install-on-mac-os-x-homebrew


```bash
brew install bazel
bazel --version
brew upgrade bazel
```

Got this error when running `bazel run :flask_solid_main`:

```bash
Collecting cryptography>=2.3
  Using cached cryptography-38.0.3.tar.gz (599 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'error'
 (  ERROR: Command errored out with exit status 1:
   command: /Library/Developer/CommandLineTools/usr/bin/python3 /private/var/tmp/_bazel_areebaaziz/16a6b220e4bfa68ccf6025606105f943/external/pypi__pip/pip/_vendor/pep517/_in_process.py get_requires_for_build_wheel /var/folders/w7/rhkylrwd7nq5rx68bfqjhgpc0000gn/T/tmptpmsl3n6
       cwd: /private/var/folders/w7/rhkylrwd7nq5rx68bfqjhgpc0000gn/T/pip-wheel-3fj9gqkv/cryptography_0a3e005dcd734a17948ab7e6883b3e83
  Complete output (29 lines):

          =============================DEBUG ASSISTANCE==========================
          If you are seeing an error here please try the following to
          successfully install cryptography:

          Upgrade to the latest pip and try again. This will fix errors for most
          users. See: https://pip.pypa.io/en/stable/installing/#upgrading-pip
          =============================DEBUG ASSISTANCE==========================

  Traceback (most recent call last):
    File "/private/var/tmp/_bazel_areebaaziz/16a6b220e4bfa68ccf6025606105f943/external/pypi__pip/pip/_vendor/pep517/_in_process.py", line 280, in <module>
      main()
    File "/private/var/tmp/_bazel_areebaaziz/16a6b220e4bfa68ccf6025606105f943/external/pypi__pip/pip/_vendor/pep517/_in_process.py", line 263, in main
      json_out['return_val'] = hook(**hook_input['kwargs'])
    File "/private/var/tmp/_bazel_areebaaziz/16a6b220e4bfa68ccf6025606105f943/external/pypi__pip/pip/_vendor/pep517/_in_process.py", line 114, in get_requires_for_build_wheel
      return hook(config_settings)
    File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages/setuptools/build_meta.py", line 146, in get_requires_for_build_wheel
      return self._get_build_requires(config_settings, requirements=['wheel'])
    File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages/setuptools/build_meta.py", line 127, in _get_build_requires
      self.run_setup()
    File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages/setuptools/build_meta.py", line 142, in run_setup
      exec(compile(code, __file__, 'exec'), locals())
    File "setup.py", line 17, in <module>
      from setuptools_rust import RustExtension
    File "/private/var/folders/w7/rhkylrwd7nq5rx68bfqjhgpc0000gn/T/pip-build-env-qj82b6e2/overlay/lib/python3.8/site-packages/setuptools_rust/__init__.py", line 1, in <module>
      from .build import build_rust
    File "/private/var/folders/w7/rhkylrwd7nq5rx68bfqjhgpc0000gn/T/pip-build-env-qj82b6e2/overlay/lib/python3.8/site-packages/setuptools_rust/build.py", line 23, in <module>
      from setuptools.command.build import build as CommandBuild  # type: ignore[import]
  ModuleNotFoundError: No module named 'setuptools.command.build'
```

It says to upgrade `pip`. 

How I fixed the issue:

1. Use Python virtual environment: `python3 -m venv .`
1. Activate virtual environment: `source bin/activate`
1. Upgrade `pip`: `pip install --upgrade pip`
1. Install from requirements.txt: `pip install -r requirements.txt`
1. Run the program: `python solid_flask_main.py`

When I ran the program, there were some missing libraries:

```bash
pip install absl-py
```

Then when I run the program I get this error:

```bash
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='solidcommunity.net', port=443): Max retries exceeded with url: /.well-known/openid-configuration (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x103d86ca0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
```

##### Nov 19, 2022

For this I will look into the code to figure out what I need to do.

In the beginning:

```python
_PORT = flags.DEFINE_integer('port', 3333, 'HTTP port to listen on')
_ISSUER = flags.DEFINE_string('issuer', 'https://solidcommunity.net/',
                              'Issuer')
```

The second line contains the issuer URL. I have a Pod Id for solidcommunity.net, but I prefer to use the Inrupt one. For now I'll leave this as is. 

**Actually - when I run it again, it works**. The server is serving the webpage at localhost port 3333. On the browser, It says I'm not logged in but provides no means to log in. 

I can't figure out how to make a simple document on the solid community server so I'll use Inrupt's. 

Ok forget it, it's not working - I changed the issuer to Inrupt and it doesn't work.

I'ma just skip this and use the Node/JavaScript version. My goal is to see what the response is anyway, and I can do this with the JavaScript library instead.

### Try JavaScript library to investigate HTTP response from a Solid server


































