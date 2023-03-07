Installation
============

Overview
--------
Before the **ifrs16** package can be used, it must be installed on your computer.
The **ifrs16** package is not hosted on `PyPi <https://pypi.org/>`_ and instead involves installing
it from a wheel. The wheel is a pre-built file of the **ifrs16** package itself.

There are three options available to get the wheel:

#. :ref:`via an URL to GitHub where it is hosted <installation:GitHub URL (Option 1)>` (*recommended*)
#. :ref:`download wheel from GitHub manually <installation:GitHub Download (Option 2)>`
#. :ref:`build the wheel yourself from the source code <installation:Build from Source Code (Option 3)>`

GitHub URL (Option 1)
---------------------
The quickest way to get started is to install the wheel directly from a release on GitHub.

#. Install using the following command:
	
	.. container:: highlight

		.. parsed-literal::
		
			pip install \ |wheel_url|\ 

The **ifrs16** package should be installed now.

You can verify that the package has been installed by listing your dependencies:

	.. code-block:: console

		pip freeze

	You should see the reference to the wheel in your output:

	.. code-block:: output

		ifrs16 @ https://github.com/bradley-smith-gpa/sphinx-test/releases/<latest-wheel-file>.whl

GitHub Download (Option 2)
--------------------------

#. Download the wheel of the latest release on GitHub and save it to a location on your computer
#. Install the wheel locally:

	.. code-block:: console

		pip install path/to/your/directory/<latest-wheel-file>.whl

The **ifrs16** package should be installed now.

You can verify that the package has been installed by listing your dependencies:

	.. code-block:: console

		pip freeze

	You should see the reference to the wheel in your output:

	.. code-block:: output

		ifrs16 @ file:///path/to/your/directory/<latest-wheel-file>.whl

	Notice that the URI starts with the ``file:///`` since we are referencing
	the wheel file locally.

Build from Source Code (Option 3)
---------------------------------
#. Clone the `ifrs16 <https://github.com/bradley-smith-gpa/ifrs16>`_ repo
#. Navigate to the repo directory in your command line (i.e. where the ``pyproject.toml`` file is),
#. Install the build package:

	.. code-block:: console

			pip install build

#. Build the wheel:

	.. code-block:: console

		python -m build

#. Navigate to the ``dist`` directory which should contain the wheel file
#. Install the wheel locally:

	.. code-block:: console

		pip install <latest-wheel-file>.whl

The **ifrs16** package should be installed now.

You can verify that the package has been installed by listing your dependencies:

	.. code-block:: console

		pip freeze

	You should see the reference to the wheel in your output:

	.. code-block:: output

		ifrs16 @ file:///path/to/your/directory/<latest-wheel-file>.whl

	Notice that the URI starts with the ``file:///`` since we are referencing
	the wheel file locally.
