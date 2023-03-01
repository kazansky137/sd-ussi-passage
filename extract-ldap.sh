:

  filter='(&(uclfournisseur=1)(!(uclinactif=*)))'

  sldap-prs.sh $filter mail | \
	grep "^mail: " | awk '{print $2;}' | tr [:upper:] [:lower:] | sort

exit
