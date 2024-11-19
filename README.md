<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Virtual Environment Setup Script</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            overflow: auto;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <h1>Python Virtual Environment Setup Script</h1>
    <p>This script automates the process of setting up a Python virtual environment and installing the required dependencies. It ensures that you have a clean and isolated environment for your Python projects.</p>

    <h2>Prerequisites</h2>
    <ul>
        <li>Ensure that Python3 is installed on your system.</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li><strong>Clone the Repository</strong>:
            <pre><code>git clone &lt;repository-url&gt;
cd &lt;repository-directory&gt;</code></pre>
        </li>
        <li><strong>Make the Script Executable</strong>:
            <pre><code>chmod +x setup_env.sh</code></pre>
        </li>
        <li><strong>Run the Script</strong>:
            <pre><code>./setup_env.sh</code></pre>
        </li>
    </ol>

    <h2>Script Details</h2>

    <h3>Steps Performed by the Script</h3>
    <ol>
        <li><strong>Check for Python3 Installation</strong>:
            <ul>
                <li>The script checks if Python3 is installed on your system. If not, it prompts you to install Python3.</li>
            </ul>
        </li>
        <li><strong>Create the Virtual Environment</strong>:
            <ul>
                <li>The script creates a virtual environment named <code>my_env</code>.</li>
            </ul>
        </li>
        <li><strong>Activate the Virtual Environment</strong>:
            <ul>
                <li>The script activates the virtual environment.</li>
            </ul>
        </li>
        <li><strong>Upgrade Pip</strong>:
            <ul>
                <li>The script upgrades <code>pip</code> to the latest version.</li>
            </ul>
        </li>
        <li><strong>Install Dependencies</strong>:
            <ul>
                <li>The script installs the following dependencies:
                    <ul>
                        <li><code>torch</code></li>
                        <li><code>torchvision</code></li>
                        <li><code>matplotlib</code></li>
                        <li><code>numpy</code></li>
                        <li><code>scipy</code></li>
                        <li><code>scikit-image</code></li>
                    </ul>
                </li>
            </ul>
        </li>
        <li><strong>Deactivate the Virtual Environment</strong>:
            <ul>
                <li>The script deactivates the virtual environment after installing the dependencies.</li>
            </ul>
        </li>
        <li><strong>Instructions for Future Activation</strong>:
            <ul>
                <li>The script provides instructions on how to activate the virtual environment in the future.</li>
            </ul>
        </li>
    </ol>

    <h3>Error Handling</h3>
    <ul>
        <li>The script includes error handling to ensure that each step is successfully completed. If any step fails, the script will exit gracefully and provide an appropriate error message.</li>
    </ul>

    <h2>Activating the Virtual Environment</h2>
    <p>To activate the virtual environment in the future, run:</p>
    <pre><code>source my_env/bin/activate</code></pre>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Please open an issue or submit a pull request.</p>

    <h2>Acknowledgments</h2>
    <p>Inspiration, etc.</p>

    <h2>Contact</h2>
    <p>For any questions or issues, please contact [Your Name] at [your-email@example.com].</p>
</body>
</html>
