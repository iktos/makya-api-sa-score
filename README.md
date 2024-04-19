# makya-api-sa-score

## Purpose

This API exposes the SA Score function to Makya.  
It is based on the code provided here https://github.com/iktos/generation-under-synthetic-constraint/tree/master/synthetic_scorers

It is provided as an example to implement a scoring API for Makya.

## Getting Started

Simply install Poetry and run the project using these commands:

```bash
poetry install
poetry run task run
```

An HTTP will be spun, listening on port 5555.

## Rebuild the image

```bash
docker build -t makya-api-sa-score:latest .
```

## Disclaimer

This source code project is provided as an example for educational and illustrative purposes only. While efforts have been made to ensure the accuracy and reliability of the code, no guarantee is made regarding its suitability for any specific purpose.

By accessing and using this source code, you agree that:

1. The code is provided "as is" without warranty of any kind, express or implied.
2. You acknowledge that you are solely responsible for any consequences resulting from the use of this code.
3. The author(s) and contributors of this code shall not be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) arising in any way out of the use of this code, even if advised of the possibility of such damage.
4. Copyright © 2024 Iktos. All rights reserved.

  
This disclaimer does not limit or exclude any liability for death or personal injury resulting from negligence, fraud, or any other liability that cannot be excluded or limited under applicable law.

Use of this source code project implies acceptance of these terms.
