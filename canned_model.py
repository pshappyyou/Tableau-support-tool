# coding=utf8
ko_cmt = "Hello Kpop"

'''
class CannedModel():
    def __init__(self):
        print("I am Canned Model")
'''

# Followup
# ConfirmationReq
# Close
# Pending
# Pass
# Spilit
# Egnyte
# FirstResponse
# AwaitLang
# TransferReg
# Feature
# Outofoffice
# Academic

## EN ##
followup_en = "Hi, ___" \
              "\n\nI am following up on this support request to see if you have had a chance to gather the information requested below. " \
              "" \
              "If so, please forward the requested information for our review." \
              "\n\nIf you would prefer, I can set this case to a 'Pending Customer' status while the requested information is gathered. " \
              "This status will prevent me from sending reminders every few days and you may respond to this support request at your convenience. " \
              "A reply to this email with the requested information will always automatically re-activate the support request and I will be notified." \
              "" \
              "\n\nPlease let us know if you would like us to keep sending reminders."
pending_en = """
Hi, ___

Following up on our recent communication on this support inquiry, I am setting this case to a 'Pending Customer' status while the requested information is gathered. This status will prevent me from sending daily reminders and you may respond to this email at your convenience. A reply to this communication will notify me, and we will continue our investigation.

Please check the Customer Portal to review your case details.
https://customer.tableau.com/

Thank you for being a valued Tableau Software customer!
"""

close_en = '''
Given the information above, we are going to move this case into a closed status.

Case details may be reviewed by visiting your Customer Portal:
https://customer.tableau.com/

This support case can always be re-opened by replying to this email. Doing so will mark the case as active, and we will happily pick up where we previously left off.

Please note that you can always open a new support incident and reference this support incident number should further assistance be needed at a later time.
'''
confirm_req_en = '''
Support - English:
Please let me know if the information provided above does not allow for the issue to be resolved. In the meantime I will be placing this case in a "Confirmation Requested" state. Please bear in mind that, should any further difficulties with this particular issue be encountered, a reply to this email will instantly bring the case to my attention.

We may send a survey to confirm that the case has been resolved. We would be grateful for any feedback specific to this issue, as well as on the overall experience with Tableau Technical Support.
'''
feature_req_en = '''
Support - EN

The ability to <<ACHIEVE DESIRED EFFECT WITH SPECIFIC FUNCTIONALITY>> is not currently built into the product. I will enter an feature request on your behalf for the Product Management team to review for possible inclusion in a future release.

Another option to provide suggestions for product enhancements is to submit an idea through our community: http://community.tableausoftware.com/community/ideas. To voice your support for the inclusion of this enhancement in a future product release, add your vote to the following Community Idea: <<LINK TO THE EXISTING COMMUNITY IDEAS>>. Providing feedback through the community forums allows other users to vote and discuss enhancement requests, and allows our development team to gauge the demand for each enhancement. Your feedback is invaluable and helps us improve our software.

Since the feature request has been submitted on your behalf, I will be moving this case into a closed status. If there is anything else we can do to help please let me know by replying to this email and this case will automatically be marked as active.

Thank you for being a valued Tableau Software customer!
'''

req_logs_en="""
Windows
- Tableau Server Zip logse. Please refer to the following link below for details how to archive Tableau Server Logs.
https://onlinehelp.tableau.com/current/server/en-us/logs_archive.htm 
- The TSM log. The tsm.log file is located in C:\\Users\\<home dir>\\.tableau\\tsm .
- The install log. The app-install.log file is located in C:\ProgramData\Tableau\Tableau Server\logs .

Linux
- Tableau Server Zip logse. Please refer to the following link below for details how to archive Tableau Server Logs.
https://onlinehelp.tableau.com/current/server-linux/en-us/logs_archive.htm 
- The TSM log. The tsm.log file is located in <home dir>/.tableau/tsm .
- The install log. The app-install.log file is located in /var/opt/tableau/tableau_server/logs .
- Tableau Server Log file: /var/opt/tableau/tableau_server/data/tabsvc/logs/
"""


## KR ##
followup_kr = """
안녕하세요 __님,

문의하신 사안에 관련해 저희가 요청한 추가 정보가 준비되었는지 알려주십시오. 만약 아래 요청된 추가 정보가 준비되었으면, 검토를 위해 보내 주시기 바랍니다.

원하신다면 요청된 추가 정보를 준비하는 동안, 이번 문의 건을 보류 상태로 설정하겠습니다.

보류 상태를 설정할 경우 계속적인 알림 이메일을 보내지 않게 되며, 원하실 때 언제든지 답변하실 수 있습니다.

이 이메일에 답변과 함께 요청된 추가 정보를 보내 주시면, 자동적으로 지원모드로 변경되며 담당자가 통보를 받게 됩니다.

계속적인 알림 이메일을 원하시면 알려주시기 바랍니다.
"""
pending_kr = """
안녕하세요 ___님,

접수하신 지원 요청 건에 대해 연락 드립니다. 이번 사안에 대해 요청한 정보가 수집되는 동안 이 사안을 보류 상태로 변경하도록 하겠습니다.

보류 상태를 설정할 경우 계속적인 알림 이메일을 보내지 않게 되며, 원하실 때 언제든지 답변하실 수 있습니다.

이 이메일에 답변과 함께 요청된 추가 정보를 보내 주시면, 자동적으로 담당자가 통보를 받게 되고 현 사안을 계속 진행하도록 하겠습니다.

접수하신 지원 요청 건에 대한 상세 사항은 아래 고객 포탈을 통해 확인하실 수 있습니다.
http://customer.tableau.com/

Tableau의 귀중한 고객이 되어 주셔서 감사합니다.
"""
close_kr = ''
confirm_req_kr=''
feature_req_kr=''
req_logs_kr='''

'''



## CN ##
followup_cn = """
我正在跟进这个支持请求， 您是否已经收集到下面要求提供的信息。 如果已经收集到要求提供的全部信息， 请发送给我们。 

如果您愿意， 我将会把此案例设置为“ 等待客户回复” 的状态，这样您可以继续收集所需的其他详细信息。进入此状态后，我将不能每隔几天发送一次提醒，您可以在方便的时候回复此支持请求。如果回复此邮件，将自动重新激活支持请求，我们也将收到通知。 

如果您希望我们继续发送提醒，请告诉我们。
"""
pending_cn = """
我们在跟进目前的技术支持案例，在等待您回复的同时，我将把这个案例改为 ‘等待客户’的状态。这个状态会停止我们每一天给您发送提醒，您可以在方便时回复此邮件。回复此邮件时我会收到通知，我们会继续这个案例的工作。

请在客户门户网站查询您提交案例的详细信息。
http://customer.tableau.com/

感谢您成为Tableau尊贵的客户！
"""


## ES ##

followup_es = '''
Estoy realizando un seguimiento sobre el caso para saber si ha podido obtener la información requerida anteriormente. Si es así, por favor envíe esta información para que continuemos con la investigación.

Si lo prefiere puedo cambiar el estado del caso a “Pendiente del cliente” mientras obtiene la información. Este estado evitará que le envíe notificaciones cada pocos días y podrá responder cuando mejor le convenga. Una respuesta a este email siempre reactivará el estado del caso y seré notificado.

Por favor indíquenos si quiere que le sigamos enviando estas notificaciones.

'''
pending_es = '''
Siguiendo con nuestras recientes comunicaciones sobre esta consulta de soporte, voy a cambiar el estado del caso a “Pendiente del cliente” mientras consigue la información solicitada. Este estado me impide enviar notificaciones diarias y puede responder a este correo electrónico a su conveniencia. Una respuesta a esta comunicación me notificará, y continuaremos con nuestra investigación.

Consulte el Portal del cliente para revisar detalles de su caso.
http://customer.tableau.com/

¡Gracias por ser un valioso cliente de Tableau Software!
'''
close_es = '''
Debido la información anterior, haremos que el estado de este caso pase a ser cerrado.

La información detallada sobre casos se puede revisar visitando su portal de clientes:
https://customer.tableau.com/

Este caso de soporte siempre se puede reabrir respondiendo a este mensaje de correo electrónico. Al hacer esto se marcará el caso como activo y con gusto lo retomaremos donde lo habíamos dejado.

Tenga en cuenta que siempre puede abrir un nuevo incidente de soporte y tener como referencia el número de este en caso de que se necesite más asistencia posteriormente.
'''
confirm_req_es = '''
Notifíqueme si la información suministrada anteriormente no permite resolver el problema. Mientras tanto, cambiaré el estado de este caso a “Confirmación solicitada”. Tenga en cuenta que, si surgen inconvenientes adicionales relacionados con este problema en particular, una respuesta a este mensaje de correo electrónico hará que el caso se presente ante mí nuevamente.

Es posible que enviemos una encuesta para confirmar que el caso se ha resuelto. Agradeceremos cualquier comentario específico relacionado con este problema y con la experiencia general de soporte técnico de Tableau.

'''
feature_req_es = ''' '''
