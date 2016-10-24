#!/bin/sh
pool=(10.152.0.51 10.152.0.52)
$cmd="cp -R /var/lib/jenkins/jobs/Publish_over_SSH/workspace/jenkinsbuild.xml /tmp/builds"
/usr/bin/fanout --noping "$pool" "$cmd";
