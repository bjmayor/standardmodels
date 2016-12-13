#coding=UTF-8
import MimeWriter
# data encoders # 数据编码
import quopri
import base64
import StringIO
import sys
TEXT = """
here comes the image you asked for.  hope
it's what you expected.
</F>"""
FILE = "samples/sample.png"
file = sys.stdout
#
# create a mime multipart writer instance
mime = MimeWriter.MimeWriter(file)

mime.addheader("Mime-Version", "1.0")
mime.startmultipartbody("mixed")
# add a text message # 加入文字信息
part = mime.nextpart()
part.addheader("Content-Transfer-Encoding", "quoted-printable")
part.startbody("text/plain")
quopri.encode(StringIO.StringIO(TEXT), file, 0)
# add an image # 加入图片
part = mime.nextpart()
part.addheader("Content-Transfer-Encoding", "base64")
part.startbody("image/jpeg")
base64.encode(open(FILE, "rb"), file)
mime.lastpart()