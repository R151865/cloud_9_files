{"filter":false,"title":"conftest.py","tooltip":"/git_practice/ib_miniprojects_backend/auth_service/tests/storages/test_user_storage_implementation/conftest.py","undoManager":{"mark":12,"position":12,"stack":[[{"start":{"row":7,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["from essentials_kit_management.constants.enums import (","    TransactionStatusEnum, TransactionTypeEnum, PaymentTypeEnum","    )",""],"id":2},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":30},"action":"remove","lines":[", Transaction, Account"],"id":3}],[{"start":{"row":78,"column":0},"end":{"row":82,"column":56},"action":"remove","lines":["","@pytest.fixture()","def create_account():","    for account in account_list:","        Account.objects.create(upi_id=account[\"upi_id\"])"],"id":3}],[{"start":{"row":78,"column":0},"end":{"row":78,"column":1},"action":"insert","lines":["\\"],"id":5}],[{"start":{"row":78,"column":0},"end":{"row":78,"column":1},"action":"remove","lines":["\\"],"id":6},{"start":{"row":77,"column":0},"end":{"row":78,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":53,"column":0},"end":{"row":67,"column":0},"action":"remove","lines":["","@pytest.fixture()","@freeze_time(\"2020-10-10\")","def create_transactions():","    for transaction in transaction_list:","        Transaction.objects.create(","            transaction_id=transaction['transaction_id'],","            user_id=transaction['user_id'],","            amount=transaction['amount'],","            status=transaction['status'],","            payment_type=transaction[\"payment_type\"],","            transaction_type=transaction[\"transaction_type\"],","            screen_shot=transaction[\"screen_shot\"],","            remark=transaction[\"remark\"])",""],"id":6}],[{"start":{"row":22,"column":0},"end":{"row":53,"column":0},"action":"remove","lines":["","transaction_list = [","    {","        \"transaction_id\": 111111,","        \"user_id\": 1,","        \"amount\": 100,","        \"status\": TransactionStatusEnum.APPROVED.value,","        \"payment_type\": PaymentTypeEnum.PHONE_PAY.value,","        \"transaction_type\": TransactionTypeEnum.CREDITED.value,","        \"screen_shot\": \"12/12\",","        \"remark\": \"wallet\"","    },","    {","        \"transaction_id\": 222222,","        \"user_id\": 1,","        \"amount\": 200,","        \"status\": TransactionStatusEnum.PENDING.value,","        \"payment_type\": PaymentTypeEnum.GOOGLE_PAY.value,","        \"transaction_type\": TransactionTypeEnum.CREDITED.value,","        \"screen_shot\": \"12/12\",","        \"remark\": \"snacks\"","    }","]","","","account_list = [","    {","        \"upi_id\": \"1234567890@SBI\"","    }","]","",""],"id":7}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"remove","lines":["",""],"id":9}],[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"remove","lines":[")"],"id":10},{"start":{"row":4,"column":8},"end":{"row":5,"column":0},"action":"remove","lines":["",""]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["r"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["e"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["s"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"remove","lines":["U"]},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "]},{"start":{"row":3,"column":46},"end":{"row":4,"column":0},"action":"remove","lines":["",""]},{"start":{"row":3,"column":45},"end":{"row":3,"column":46},"action":"remove","lines":["("]},{"start":{"row":3,"column":44},"end":{"row":3,"column":45},"action":"remove","lines":[" "]},{"start":{"row":3,"column":43},"end":{"row":3,"column":44},"action":"remove","lines":["t"]}],[{"start":{"row":3,"column":43},"end":{"row":3,"column":44},"action":"insert","lines":["t"],"id":11}],[{"start":{"row":3,"column":44},"end":{"row":3,"column":45},"action":"insert","lines":[" "],"id":12},{"start":{"row":3,"column":45},"end":{"row":3,"column":46},"action":"insert","lines":["U"]},{"start":{"row":3,"column":46},"end":{"row":3,"column":47},"action":"insert","lines":["s"]},{"start":{"row":3,"column":47},"end":{"row":3,"column":48},"action":"insert","lines":["e"]},{"start":{"row":3,"column":48},"end":{"row":3,"column":49},"action":"insert","lines":["r"]}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":30},"action":"remove","lines":["essentials_kit_management"],"id":13},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["a"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["u"]}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":7},"action":"remove","lines":["au"],"id":14},{"start":{"row":3,"column":5},"end":{"row":3,"column":17},"action":"insert","lines":["auth_service"]}]]},"ace":{"folds":[{"start":{"row":23,"column":19},"end":{"row":28,"column":47},"placeholder":"..."}],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":20},"end":{"row":17,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1593702691424,"hash":"a38b8116a70fba57cfa68b5a3bbc73916e10ac41"}