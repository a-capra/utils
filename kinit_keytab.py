from krbcontext.context import krbContext

with krbContext(using_keytab=True, principal='[username]@[REALM]', keytab_file='/etc/security/keytabs/[name].keytab', ccache_file='/tmp/krb5cc_pid_appname'):
    pass
