BODY = """
print 'the ant, an introduction'
"""
code =  compile(BODY,"<script>", "exec")
print code
exec code