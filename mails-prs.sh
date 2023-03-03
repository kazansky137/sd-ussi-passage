:

# set -x

  base=mails
  mprs=mails-prs
  file=$base/$mprs-$(date +%y%m%d).txt

  [ ! -h $base ] && { echo Missing $base symlink; exit 1; }

  [ -f $file ] && { echo File $file already exists; exit 1; }

  ./extract-ldap.sh > $file

exit 0
