# gh


```bash
MacBookPro ~/projects/gh master
λ gh --help
usage: gh [-h] [-n] [-b BRANCH] [-r REMOTE]

Open browser to git remote

optional arguments:
  -h, --help            show this help message and exit
  -n, --no-launch       Don't launch the browser
  -b BRANCH, --branch BRANCH
                        branch to open instead of current
  -r REMOTE, --remote REMOTE
                        Use remote by this name (Default: origin)
```

## Uses

```bash
MacBookPro ~ -
λ cd ~/projects/gh
MacBookPro ~/projects/gh master
λ gh
http://github.com/brettof86/gh
```

*launches the default browser to the url printed*

```bash
MacBookPro ~/projects/gh master
λ gh --branch ReleaseBranch
http://github.com/brettof86/gh/tree/ReleaseBranch
```
