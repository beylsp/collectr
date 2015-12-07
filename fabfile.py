from fabric.api import runs_once, lcd, local, task


@task
@runs_once
def register_deployment(git_path):
    with(lcd(git_path)):
        revision = local('git log -n 1 --pretty="format:%H"', capture=True)
        branch = local('git rev-parse --abbrev-ref HEAD', capture=True)
        local('curl https://intake.opbeat.com/api/v1/organizations/'
              'c6b1b6f06dab409db01224faa85c9887/apps/209b15af04/releases/'
              ' -H "Authorization: '
              'Bearer b5b3969552cbaf97b75e94014bff7108d8c0be6b"'
              ' -d rev="{}"'
              ' -d branch="{}"'
              ' -d status=completed'.format(revision, branch))
