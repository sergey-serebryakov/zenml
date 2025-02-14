#  Copyright (c) ZenML GmbH 2020. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

import os
from typing import Optional

import click
import git

from zenml.cli.cli import cli
from zenml.cli.utils import confirmation
from zenml.core.repo import Repository
from zenml.utils.analytics_utils import INITIALIZE_REPO, track


@cli.command("init", help="Initialize zenml on a given path.")
@click.option("--repo_path", type=click.Path(exists=True))
@click.option("--analytics_opt_in", "-a", type=click.BOOL)
@track(event=INITIALIZE_REPO)
def init(
    repo_path: Optional[str],
    analytics_opt_in: bool = True,
) -> None:
    """Initialize ZenML on given path.

    Args:
      repo_path: Path to the repository.
      analytics_opt_in: (Default value = True)

    Raises:
        InvalidGitRepositoryError: If repo is not a git repo.
        AssertionError
    """
    if repo_path is None:
        repo_path = os.getcwd()

    click.echo(f"Initializing at {repo_path}")

    try:
        Repository.init_repo(
            repo_path=repo_path,
            analytics_opt_in=analytics_opt_in,
        )
        click.echo(f"ZenML repo initialized at {repo_path}")
    except git.InvalidGitRepositoryError:  # type: ignore[attr-defined]
        click.echo(
            f"{repo_path} is not a valid git repository! Please "
            f"initialize ZenML within a git repository using "
            f"`git init `"
        )
    except AssertionError as e:
        click.echo(f"{e}")


@cli.command("clean")
@click.option("--yes", "-y", type=click.BOOL, default=False)
def clean(yes: bool = False) -> None:
    """Clean everything in repository.

    Args:
      yes: bool:  (Default value = False)

    Returns:

    """
    if not yes:
        _ = confirmation(
            "This will completely delete all pipelines, their associated "
            "artifacts and metadata ever created in this ZenML repository. "
            "Are you sure you want to proceed?"
        )

    click.echo("Not implemented for this version")
    # if confirm:
    #     repo.clean()
