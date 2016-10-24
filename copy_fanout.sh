#!/bin/sh
pool=(10.152.0.51 10.152.0.52)
$cmd="scp bannam@192.168.110.15:/var/lib/jenkins/jobs/Publish_over_SSH/workspace/jenkinsbuild.xml bannam@$pool:/tmp/builds"
/usr/bin/fanout --noping "$pool" "$cmd";
