<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/styles/default.min.css">
  </head>
  <body>
    <p>::page{title="Building a Tekton Pipeline"}</p>
    <p><strong>Estimated time needed:</strong> 40 minutes</p>
    <p>Welcome to the hands-on lab for <strong>Building a Tekton Pipeline</strong>. In this lab, you will create a simple Tekton pipeline with one task in Step 1 and then add a parameter to it in Step 4. You will learn best practices for structuring a Tekton pipeline project and how to author Tekton pipelines and tasks so that they are easy to use and parameterize. You will see that Tekton allows you to reuse your pipeline-as-code artifacts, and you will look at practical approaches to publishing your pipeline and task definitions to a Git repository.</p>
    <h2>Learning Objectives</h2>
    <p>After completing this lab, you will be able to:</p>
    <ul>
      <li>Create a base pipeline and task to echo a message.</li>
      <li>Apply parameters to the task and pipeline.</li>
      <li>Apply additional parameters to a pipeline to clone a Git repository.</li>
    </ul>
    <h2>Prerequisites</h2>
    <p>You will need the following to complete the exercises in this lab:</p>
    <ul>
      <li>A basic understanding of YAML</li>
      <li>A GitHub account</li>
      <li>An intermediate-level knowledge of CLIs</li>
    </ul>
    <hr>
    <p>::page{title="Set Up the Lab Environment"}</p>
    <p>You have a little preparation to do before you can start the lab.</p>
    <h2>Open a Terminal</h2>
    <p>Open a terminal window by using the menu in the editor: Terminal > New Terminal.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0215EN-SkillsNetwork/images/01_terminal.png" alt="Terminal">
    </p>
    <p>In the terminal, if you are not already in the <code>/home/project</code> folder, change to your project folder now.</p>
    <pre><code class="hljs language-bash"><span class="hljs-built_in">cd</span> /home/project
</code></pre>
    <h2>Clone the Code Repo</h2>
    <p>Now, get the code that you need to test. To do this, use the <code>git clone</code> command to clone the Git repository:</p>
    <pre><code class="hljs language-bash">git <span class="hljs-built_in">clone</span> https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git
</code></pre>
    <p>Your output should look similar to the image below:</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0215EN-SkillsNetwork/images/01_git_clone_code.png" alt="Git Clone">
    </p>
    <h2>Change to the Labs Directory</h2>
    <p>Once you have cloned the repository, change to the labs directory.</p>
    <pre><code class="hljs language-bash"><span class="hljs-built_in">cd</span> wtecc-CICD_PracticeCode/labs/01_base_pipeline/
</code></pre>
    <h2>Navigate to the Labs Folder</h2>
    <p>Navigate to the <code>labs/01_base_pipeline</code> folder in left explorer panel. All of your work will be completed with the files in this folder.</p>
    <p>
      <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0215EN-SkillsNetwork/images/01_file_explorer.png" alt="File Explorer">
    </p>
    <p>You are now ready to start the lab.</p>
    <h3>Optional</h3>
    <p>If working in the terminal becomes difficult because the command prompt is very long, you can shorten the prompt using the following command:</p>
    <pre><code class="hljs language-bash"><span class="hljs-built_in">export</span> PS1=<span class="hljs-string">"[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "</span>
</code></pre>
    <hr>
    <p>::page{title="Step 1: Create an echo Task"}</p>
    <p>In true computer programming tradition, the first task you create will echo "Hello World!" to the console.</p>
    <p>There is starter code in the <code>labs/01_base_pipeline</code> folder for a task and a pipeline. Navigate to this folder in left explorer panel, and open the <code>tasks.yaml</code> file to edit it:</p>
    <p>::openFile{path="/home/project/wtecc-CICD_PracticeCode/labs/01_base_pipeline/tasks.yaml"}</p>
    <p>It should look like this:</p>
    <pre><code class="hljs language-yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Task</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">&#x3C;place-name-here></span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">steps:</span>
</code></pre>
    <p>Using the same steps that you learned in the video to create the <strong>checkout</strong> task, you will now create a <strong>hello-world</strong> task.</p>
    <h3>Your Task</h3>
    <ol>
      <li>
        <p>The first thing you want to do is give the task a good name. Change <code>&#x3C;place-name-here></code> to <code>hello-world</code>.</p>
      </li>
      <li>
        <p>The next thing is to add a step. Remember from the video that steps that run a single command need to include <code>name</code>, <code>image</code>, <code>command</code>, and <code>args</code>. Make the name <code>echo</code>, use the image <code>alpine:3</code>, have the command be <code>[/bin/echo]</code> and the args be <code>["Hello World"]</code>.</p>
      </li>
    </ol>
    <h3>Hint</h3>
    <details>
      <summary>Click here for a hint.</summary>Add a step under the `steps:` tag. Since there can be multiple steps, each one starts with a dash `-` to identify it as an item in a `yaml` list.
      <pre><code class="hljs language-yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">image:</span> {<span class="hljs-string">image</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">command:</span> {<span class="hljs-string">command</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">args:</span> {<span class="hljs-string">args</span> <span class="hljs-string">here</span>}
</code></pre>
    </details>
    <p>Double-check that your work matches the solution below.</p>
    <h3>Solution</h3>
    <details>
      <summary>Click here for the answer.</summary>
      <pre><code class="hljs language-yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Task</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">hello-world</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">image:</span> <span class="hljs-string">alpine:3</span>
      <span class="hljs-attr">command:</span> [<span class="hljs-string">/bin/echo</span>]
      <span class="hljs-attr">args:</span> [<span class="hljs-string">"Hello World!"</span>]
</code></pre>
    </details>
    <p>Apply it to the cluster:</p>
    <pre><code class="hljs language-bash">kubectl apply -f tasks.yaml
</code></pre>
    <hr>
    <p>::page{title="Step 2: Create a hello-pipeline Pipeline"}</p>
    <p>Next, you will create a very simple pipeline that only calls the <code>hello-world</code> task that you just created. Navigate to this folder in left explorer panel, and open the <code>pipeline.yaml</code> file to edit it:</p>
    <p>::openFile{path="/home/project/wtecc-CICD_PracticeCode/labs/01_base_pipeline/pipeline.yaml"}</p>
    <p>It should look like this:</p>
    <pre><code class="hljs language-yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Pipeline</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">&#x3C;place-name-here></span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">tasks:</span>
</code></pre>
    <p>Using the same steps that you learned in the video to create the <strong>ci-pipeline</strong> pipeline, you will now create a <strong>hello-pipeline</strong> pipeline.</p>
    <h3>Your Task</h3>
    <ol>
      <li>
        <p>The first thing you want to do is give the pipeline a good name. Change <code>&#x3C;place-name-here></code> to <code>hello-pipeline</code>.</p>
      </li>
      <li>
        <p>The next thing is to add a reference to the hello-world task you just created. Remember from the video that task needs a <code>name:</code> for the pipeline task, and a <code>taskRef:</code>, with a <code>name:</code> tag under it set to the name of the task you are referencing. Set the name of the pipeline task to <code>hello</code> and the name of the task you are referencing as <code>hello-world</code>.</p>
      </li>
    </ol>
    <h3>Hint</h3>
    <details>
      <summary>Click here for a hint.</summary>Add a task under the `tasks:` tag. Since there can be multiple tasks, each one starts with a dash `-` to identify it as an item in a `yaml` list.
      <pre><code class="hljs language-yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> {<span class="hljs-string">task</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
</code></pre>
    </details>
    <p>Double-check that your work matches the solution below.</p>
    <h3>Solution</h3>
    <details>
      <summary>Click here for the answer.</summary>
      <pre><code class="hljs language-yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Pipeline</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">hello-pipeline</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">hello</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">hello-world</span>
</code></pre>
    </details>
    <p>Apply it to the cluster:</p>
    <pre><code class="hljs language-bash">kubectl apply -f pipeline.yaml
</code></pre>
    <p>You are now ready to run your pipeline and see if it works.</p>
    <hr>
    <p>::page{title="Step 3: Run the hello-pipeline"}</p>
    <p>Run the pipeline using the Tekton CLI:</p>
    <pre><code class="hljs language-bash">tkn pipeline start --showlog hello-pipeline
</code></pre>
    <p>You should see the output:</p>
    <pre><code class="hljs language-vim">PipelineRun started: hello-pipeline-run-<span class="hljs-number">9</span>vkbb
Waiting <span class="hljs-keyword">for</span> logs <span class="hljs-keyword">to</span> <span class="hljs-keyword">be</span> available...
[hello : <span class="hljs-keyword">echo</span>] Hello World!
</code></pre>
    <p>Congratulations! You just ran your first pipeline from a pipeline and task that you created.</p>
    <hr>
    <p>::page{title="Step 4: Add a parameter to the task"}</p>
    <p>Hopefully the hello-world task has given you a sense for how pipelines call tasks. Now it is time to make that task a little more useful by making it print any message that you want, not just "Hello World".</p>
    <p>To do this, you will add a parameter called <code>message</code> to the task and use that parameter as the message that it echoes. You will also rename the task to <code>echo</code>.</p>
    <p>Edit the <code>tasks.yaml</code> file to add the parameter to both the input and the echo command:</p>
    <p>::openFile{path="/home/project/wtecc-CICD_PracticeCode/labs/01_base_pipeline/tasks.yaml"}</p>
    <h3>Your Task</h3>
    <ol>
      <li>
        <p>Change the name of the task from <code>hello-world</code> to <code>echo</code> to more acurately reflect its new functionality, by changing the <code>name:</code> in the <code>metadata:</code> section.</p>
      </li>
      <li>
        <p>Add a <code>params:</code> section to the task with a parameter that has a <code>name:</code> of "message", a <code>type:</code> of "string", and a <code>description</code> of "The message to echo".</p>
      </li>
      <li>
        <p>Change the name of the step from <code>echo</code> to <code>echo-message</code> to better describe its new functionality.</p>
      </li>
      <li>
        <p>Modify the <code>args:</code> tag to use the message parameter you just created.</p>
      </li>
    </ol>
    <h3>Hint</h3>
    <details>
      <summary>Click here for a hint.</summary>Add a `params:` section under the `spec:` tag. Since there can be multiple parameters, each one starts with a dash `-` to identify it as an item in a `yaml` list.
      <p>The reference to the message parameter should be <code>$(params.message)</code>.</p>
      <pre><code class="hljs language-yaml"><span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> {<span class="hljs-string">change</span> <span class="hljs-string">the</span> <span class="hljs-string">task</span> <span class="hljs-string">name</span>}
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">description:</span> {<span class="hljs-string">description</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">type:</span> {<span class="hljs-string">type</span> <span class="hljs-string">here</span>}
  <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">echo-message</span>
      <span class="hljs-attr">image:</span> <span class="hljs-string">alpine:3</span>
      <span class="hljs-attr">command:</span> [<span class="hljs-string">/bin/echo</span>]
      <span class="hljs-attr">args:</span> {<span class="hljs-string">place</span> <span class="hljs-string">parameter</span> <span class="hljs-string">reference</span> <span class="hljs-string">here</span>}
</code></pre>
    </details>
    <p>Double-check that your work matches the solution below.</p>
    <h3>Solution</h3>
    <details>
      <summary>Click here for the answer.</summary>
      <pre><code class="hljs language-yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Task</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
      <span class="hljs-attr">description:</span> <span class="hljs-string">The</span> <span class="hljs-string">message</span> <span class="hljs-string">to</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">type:</span> <span class="hljs-string">string</span>
  <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">echo-message</span>
      <span class="hljs-attr">image:</span> <span class="hljs-string">alpine:3</span>
      <span class="hljs-attr">command:</span> [<span class="hljs-string">/bin/echo</span>]
      <span class="hljs-attr">args:</span> [<span class="hljs-string">"$(params.message)"</span>]
</code></pre>
    </details>
    <p>Apply the new task definition to the cluster:</p>
    <pre><code class="hljs language-bash">kubectl apply -f tasks.yaml
</code></pre>
    <hr>
    <p>::page{title="Step 5: Update the hello-pipeline"}</p>
    <p>You now need to update the pipeline to pass the message that you want to send to the <code>echo</code> task so that it can echo the message to the console.</p>
    <p>Edit the <code>pipeline.yaml</code> file to add the parameter:</p>
    <p>::openFile{path="/home/project/wtecc-CICD_PracticeCode/labs/01_base_pipeline/pipeline.yaml"}</p>
    <h3>Your Task</h3>
    <ol>
      <li>
        <p>Add a <code>params:</code> section to the pipeline under <code>spec:</code>, with a parameter that has a <code>name:</code> of "message".</p>
      </li>
      <li>
        <p>Change the <code>name:</code> of the <code>taskRef:</code> from <code>hello-world</code> to the new <code>echo</code> task.</p>
      </li>
      <li>
        <p>Add a <code>params:</code> section to the task, with a parameter that has a <code>name:</code> of "message" and a <code>value:</code> that is a reference to the pipeline parameter for <code>params.message</code>.</p>
      </li>
    </ol>
    <h3>Hint</h3>
    <details>
      <summary>Click here for a hint.</summary>Specify the value of message params in tasks as "$(params.message)".
      <pre><code class="hljs language-yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">hello</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> {<span class="hljs-string">change</span> <span class="hljs-string">parameter</span> <span class="hljs-string">value</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">params:</span>
        <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">task</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
          <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.message)"</span>
</code></pre>
    </details>
    <p>Double-check that your work matches the solution below.</p>
    <h3>Solution</h3>
    <details>
      <summary>Click here for the answer.</summary>
      <pre><code class="hljs language-yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Pipeline</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">hello-pipeline</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">hello</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">params:</span>
        <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
          <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.message)"</span>
</code></pre>
    </details>
    <p>Apply it to the cluster:</p>
    <pre><code class="hljs language-bash">kubectl apply -f pipeline.yaml
</code></pre>
    <hr>
    <p>::page{title="Step 6: Run the message-pipeline"}</p>
    <p>Run the pipeline using the Tekton CLI:</p>
    <pre><code class="hljs language-bash">tkn pipeline start hello-pipeline \
    --showlog  \
    -p message=<span class="hljs-string">"Hello Tekton!"</span>
</code></pre>
    <p>You should see the output:</p>
    <pre><code class="hljs language-vim">PipelineRun started: hello-pipeline-run-<span class="hljs-number">9</span>qf42
Waiting <span class="hljs-keyword">for</span> logs <span class="hljs-keyword">to</span> <span class="hljs-keyword">be</span> available...
[hello : <span class="hljs-keyword">echo</span>-message] Hello Tekton!
</code></pre>
    <p>Congratulations! You just created and ran a pipeline that requires a parameter.</p>
    <hr>
    <p>::page{title="Step 7: Create a checkout Task"}</p>
    <p>In this step, you will combine your knowledge of running a command in a container with your knowledge of passing parameters, to create a task that checks out your code from GitHub as the first step in a CD pipeline.</p>
    <h2>Create checkout task</h2>
    <p>You can have multiple definitions in a single yaml file by separating them with three dashes <code>---</code> on a single line. In this step, you will add a new task to <code>tasks.yaml</code> that uses the <code>bitnami/git:latest</code> image to run the <code>git</code> command passing in the branch name and URL of the repo you want to clone.</p>
    <p>Open the <code>tasks.yaml</code> file to create a new task:</p>
    <p>::openFile{path="/home/project/wtecc-CICD_PracticeCode/labs/01_base_pipeline/tasks.yaml"}</p>
    <p>Add three dashes on a separate line:</p>
    <pre><code class="hljs language-yaml"><span class="hljs-meta">---
</span></code></pre>
    <p>You are now ready to add your new task.</p>
    <h3>Your Task</h3>
    <p>Your new task will create a Tekton task that accepts a repository URL and a branch name and calls <code>git clone</code> to clone your source code.</p>
    <ol>
      <li>
        <p>Create a new task and name it <code>checkout</code>.</p>
      </li>
      <li>
        <p>Add a parameter named <code>repo-url</code> with a <code>type:</code> of string and a <code>description:</code> of "The URL of the git repo to clone".</p>
      </li>
      <li>
        <p>Add a second parameter named <code>branch</code> with a <code>type:</code> of string and a <code>description:</code> of "The branch to clone".</p>
      </li>
      <li>
        <p>Add a step with the <code>name:</code> "checkout" that uses the <code>bitnami/git:latest</code> image to run the <code>git</code> command by specifying <code>clone</code> and <code>--branch</code> parameters and passing both the params created in spec as the arguments.</p>
      </li>
    </ol>
    <h3>Hint</h3>
    <details>
      <summary>Click here for a hint.</summary>Pass arguments to the checkout task as ["clone", "--branch", "$(params.branch)", "$(params.repo-url)"].
      <pre><code class="hljs language-yaml"><span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Task</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> {<span class="hljs-string">name</span> <span class="hljs-string">of</span> <span class="hljs-string">task</span> <span class="hljs-string">here</span>}
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">1st</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">description:</span> {<span class="hljs-string">1st</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">type:</span> <span class="hljs-string">string</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">2nd</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">description:</span> {<span class="hljs-string">2nd</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">type:</span> <span class="hljs-string">string</span>
  <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">step</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">image:</span> {<span class="hljs-string">image</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">command:</span> [{<span class="hljs-string">command</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}]
      <span class="hljs-attr">args:</span> [{<span class="hljs-string">arguments</span> <span class="hljs-string">here</span>}]
</code></pre>
    </details>
    <p>Double-check that your work matches the solution below.</p>
    <h3>Solution</h3>
    <details>
      <summary>Click here for the answer.</summary>
      <pre><code class="hljs language-yaml"><span class="hljs-meta">---</span>
<span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Task</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">checkout</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">repo-url</span>
      <span class="hljs-attr">description:</span> <span class="hljs-string">The</span> <span class="hljs-string">URL</span> <span class="hljs-string">of</span> <span class="hljs-string">the</span> <span class="hljs-string">git</span> <span class="hljs-string">repo</span> <span class="hljs-string">to</span> <span class="hljs-string">clone</span>
      <span class="hljs-attr">type:</span> <span class="hljs-string">string</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">branch</span>
      <span class="hljs-attr">description:</span> <span class="hljs-string">The</span> <span class="hljs-string">branch</span> <span class="hljs-string">to</span> <span class="hljs-string">clone</span>
      <span class="hljs-attr">type:</span> <span class="hljs-string">string</span>
  <span class="hljs-attr">steps:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">checkout</span>
      <span class="hljs-attr">image:</span> <span class="hljs-string">bitnami/git:latest</span>
      <span class="hljs-attr">command:</span> [<span class="hljs-string">git</span>]
      <span class="hljs-attr">args:</span> [<span class="hljs-string">"clone"</span>, <span class="hljs-string">"--branch"</span>, <span class="hljs-string">"$(params.branch)"</span>, <span class="hljs-string">"$(params.repo-url)"</span>]
</code></pre>
    </details>
    <p>Apply it to the cluster:</p>
    <pre><code class="hljs language-bash">kubectl apply -f tasks.yaml
</code></pre>
    <p>Your output should look like this:</p>
    <pre><code class="hljs language-txt">task.tekton.dev/echo configured
task.tekton.dev/checkout created
</code></pre>
    <p>The <code>echo</code> task was unchanged and the <code>checkout</code> task has been created.</p>
    <hr>
    <p>::page{title="Step 8: Create the cd-pipeline Pipeline"}</p>
    <p>Finally, you will create a pipeline called <code>cd-pipeline</code> to be the starting point of your Continuous Delivery pipeline.</p>
    <p>Open the <code>pipeline.yaml</code> file to create a new pipeline called <code>cd-pipeline</code>:</p>
    <p>::openFile{path="/home/project/wtecc-CICD_PracticeCode/labs/01_base_pipeline/pipeline.yaml"}</p>
    <p>You can use <code>---</code> on a separate line to separate your new pipeline, or you can modify the existing pipeline to look like the new one.</p>
    <h3>Your Task</h3>
    <ol>
      <li>
        <p>Create a new pipeline and name it <code>cd-pipeline</code>.</p>
      </li>
      <li>
        <p>Add two parameters named <code>repo-url</code> and <code>branch</code>.</p>
      </li>
      <li>
        <p>Set the <code>default:</code> for <strong>branch</strong> to "master".</p>
      </li>
      <li>
        <p>Add a task with the <code>name:</code> "clone" that has a <code>taskRef:</code> to the <code>checkout</code> task that you just created.</p>
      </li>
      <li>
        <p>Add the two parameters <code>repo-url</code> and <code>branch</code> to the task, mapping them back to the pipeline parameters of the same name.</p>
      </li>
    </ol>
    <h3>Hint</h3>
    <details>
      <summary>Click here for a hint.</summary>Add params of name `repo-url` and `branch` with values as "$(params.repo-url)" and "$(params.branch)" to the `clone` task.
      <pre><code class="hljs language-yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">1st</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">2nd</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">default:</span> {<span class="hljs-string">default</span> <span class="hljs-string">value</span> <span class="hljs-string">here</span>}
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">pipeline</span> <span class="hljs-string">task</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> {<span class="hljs-string">Task</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">1st</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
        <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.repo-url)"</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">2nd</span> <span class="hljs-string">parameter</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
        <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.branch)"</span>
</code></pre>
    </details>
    <p>Double-check that your work matches the solution below.</p>
    <h3>Solution</h3>
    <details>
      <summary>Click here for the answer.</summary>
      <pre><code class="hljs language-yaml"><span class="hljs-meta">---</span>
<span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Pipeline</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">cd-pipeline</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">repo-url</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">branch</span>
      <span class="hljs-attr">default:</span> <span class="hljs-string">"master"</span>
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">clone</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">checkout</span>
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">repo-url</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.repo-url)"</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">branch</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.branch)"</span>
</code></pre>
    </details>
    <p>Apply it to the cluster:</p>
    <pre><code class="hljs language-bash">kubectl apply -f pipeline.yaml
</code></pre>
    <hr>
    <p>::page{title="Step 9: Run the cd-pipeline"}</p>
    <p>Run the pipeline using the Tekton CLI:</p>
    <pre><code class="hljs language-bash">tkn pipeline start cd-pipeline \
    --showlog \
    -p repo-url=<span class="hljs-string">"https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git"</span> \
    -p branch=<span class="hljs-string">"main"</span>
</code></pre>
    <p>The output should look like this:</p>
    <pre><code class="hljs language-crmsh">PipelineRun <span class="hljs-literal">started</span>: cd-pipeline-run-rf6zp
Waiting for logs to be available...
[<span class="hljs-keyword">clone</span> <span class="hljs-title">: checkout</span>] Cloning into 'wtecc-CICD_PracticeCode'...
</code></pre>
    <hr>
    <p>::page{title="Step 10: Fill Out cd-pipeline with Placeholders"}</p>
    <p>In this final step, you will fill out the rest of the pipeline with calls to the <code>echo</code> task to simply display a message for now. You will replace these "placeholder" tasks with real ones in future labs.</p>
    <p>Update the pipeline.yaml file to include four placeholder tasks.</p>
    <p>::openFile{path="/home/project/wtecc-CICD_PracticeCode/labs/01_base_pipeline/pipeline.yaml"}</p>
    <p>Now you will add four tasks to the pipeline to lint, unit test, build, and deploy. All of these pipeline tasks will reference the <code>echo</code> task for now.</p>
    <h3>Your Task</h3>
    <p>Create a pipeline task for each of these:</p>
    <table>
      <thead>
        <tr>
          <th>Task Name</th>
          <th>Build After</th>
          <th>Message</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>lint</td>
          <td>clone</td>
          <td>Calling Flake8 linter...</td>
        </tr>
        <tr>
          <td>tests</td>
          <td>lint</td>
          <td>Running unit tests with PyUnit...</td>
        </tr>
        <tr>
          <td>build</td>
          <td>tests</td>
          <td>Building image for $(params.repo-url) ...</td>
        </tr>
        <tr>
          <td>deploy</td>
          <td>build</td>
          <td>Deploying $(params.branch) branch of $(params.repo-url) ...</td>
        </tr>
      </tbody>
    </table>
    <h3>Hint</h3>
    <details>
      <summary>Click here for a hint.</summary>Add params of name `repo-url` and `branch` with values as "$(params.repo-url)" and "$(params.branch)" to the `clone` task.
      <pre><code class="hljs language-yaml"><span class="hljs-attr">spec:</span>
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> {<span class="hljs-string">pipeline</span> <span class="hljs-string">task</span> <span class="hljs-string">name</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
        <span class="hljs-attr">value:</span> {<span class="hljs-string">message</span> <span class="hljs-string">to</span> <span class="hljs-string">display</span> <span class="hljs-string">here</span>}
      <span class="hljs-attr">runAfter:</span>
        <span class="hljs-bullet">-</span> {<span class="hljs-string">name</span> <span class="hljs-string">of</span> <span class="hljs-string">previous</span> <span class="hljs-string">task</span>}

	<span class="hljs-string">...</span>
</code></pre>
    </details>
    <p>You now have a base pipeline to build the rest of your tasks into.</p>
    <p>Double-check that your work matches the solution below.</p>
    <h3>Solution</h3>
    <details>
      <summary>Click here for the answer.</summary>
      <pre><code class="hljs language-yaml"><span class="hljs-meta">---</span>
<span class="hljs-attr">apiVersion:</span> <span class="hljs-string">tekton.dev/v1beta1</span>
<span class="hljs-attr">kind:</span> <span class="hljs-string">Pipeline</span>
<span class="hljs-attr">metadata:</span>
  <span class="hljs-attr">name:</span> <span class="hljs-string">cd-pipeline</span>
<span class="hljs-attr">spec:</span>
  <span class="hljs-attr">params:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">repo-url</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">branch</span>
      <span class="hljs-attr">default:</span> <span class="hljs-string">"master"</span>
  <span class="hljs-attr">tasks:</span>
    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">clone</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">checkout</span>
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">repo-url</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.repo-url)"</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">branch</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"$(params.branch)"</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">lint</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"Calling Flake8 linter..."</span>
      <span class="hljs-attr">runAfter:</span>
        <span class="hljs-bullet">-</span> <span class="hljs-string">clone</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">tests</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"Running unit tests with PyUnit..."</span>
      <span class="hljs-attr">runAfter:</span>
        <span class="hljs-bullet">-</span> <span class="hljs-string">lint</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">build</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"Building image for $(params.repo-url) ..."</span>
      <span class="hljs-attr">runAfter:</span>
        <span class="hljs-bullet">-</span> <span class="hljs-string">tests</span>

    <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">deploy</span>
      <span class="hljs-attr">taskRef:</span>
        <span class="hljs-attr">name:</span> <span class="hljs-string">echo</span>
      <span class="hljs-attr">params:</span>
      <span class="hljs-bullet">-</span> <span class="hljs-attr">name:</span> <span class="hljs-string">message</span>
        <span class="hljs-attr">value:</span> <span class="hljs-string">"Deploying $(params.branch) branch of $(params.repo-url) ..."</span>
      <span class="hljs-attr">runAfter:</span>
        <span class="hljs-bullet">-</span> <span class="hljs-string">build</span>
</code></pre>
    </details>
    <p>Apply it to the cluster:</p>
    <pre><code class="hljs language-bash">kubectl apply -f pipeline.yaml
</code></pre>
    <hr>
    <p>::page{title="Step 11: Run the cd-pipeline"}</p>
    <p>Run the pipeline using the Tekton CLI:</p>
    <pre><code class="hljs language-bash">tkn pipeline start cd-pipeline \
    --showlog \
    -p repo-url=<span class="hljs-string">"https://github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git"</span> \
    -p branch=<span class="hljs-string">"main"</span>
</code></pre>
    <p>The output will look like this:</p>
    <pre><code class="hljs language-json">PipelineRun started: cd-pipeline-run-wvfzx
Waiting for logs to be available...
[clone : checkout] Cloning into 'wtecc-CICD_PracticeCode'...

[lint : echo-message] Calling Flake8 linter...

[tests : echo-message] Running unit tests with PyUnit...

[build : echo-message] Building image for https:<span class="hljs-comment">//github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git ...</span>

[deploy : echo-message] Deploying main branch of https:<span class="hljs-comment">//github.com/ibm-developer-skills-network/wtecc-CICD_PracticeCode.git ...</span>
</code></pre>
    <p>::page{title="Conclusion"}</p>
    <p>Congratulations! You are now able to create a Tekton pipeline and pass parameters to a pipeline.</p>
    <p>In this lab, you learned how to create a base pipeline, specify and pass parameteres to a task and pipeline. You learned how to modify your pipeline to reference the task and configure its parameters. You also learned how to pass additional parameters to a pipeline and how to run it to echo and clone a Git repository.</p>
    <h2>Next Steps</h2>
    <p>You will learn and use GitHub Triggers in the next lab.</p>
    <h2>Author(s)</h2>
    <p>
      Tapas Mandal
      <a href="https://www.coursera.org/instructor/johnrofrano?utm_medium=Exinfluencer&#x26;utm_source=Exinfluencer&#x26;utm_content=000026UJ&#x26;utm_term=10006555&#x26;utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMCD0215ENSkillsNetwork35576036-2022-01-01" target="_blank" rel="external">John J. Rofrano</a>
    </p>
    <h3>Other Contributor(s)</h3>
    <h2>Change Log</h2>
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Version</th>
          <th>Changed by</th>
          <th>Change Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2022-07-24</td>
          <td>0.1</td>
          <td>Tapas Mandal</td>
          <td>Initial version created</td>
        </tr>
        <tr>
          <td>2022-07-28</td>
          <td>0.2</td>
          <td>John Rofrano</td>
          <td>Added additional instructions</td>
        </tr>
        <tr>
          <td>2022-07-31</td>
          <td>0.3</td>
          <td>Steve Ryan</td>
          <td>ID review</td>
        </tr>
        <tr>
          <td>2022-08-01</td>
          <td>0.4</td>
          <td>Beth Larsen</td>
          <td>QA review</td>
        </tr>
        <tr>
          <td>---</td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
      </tbody>
    </table>
    <script>window.addEventListener('load', function() {
snFaculty.inject();
});</script>
    <script src="https://skills-network-assets.s3.us.cloud-object-storage.appdomain.cloud/scripts/inject.43989f87.js"></script>
    <script src="https://unpkg.com/@highlightjs/cdn-assets@10.7.1/highlight.min.js"></script>
    <script src="https://unpkg.com/highlightjs-badge@0.1.9/highlightjs-badge.min.js"></script>
  </body>
</html>
