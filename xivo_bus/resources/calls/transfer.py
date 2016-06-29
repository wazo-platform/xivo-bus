# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from __future__ import unicode_literals


class BaseTransferEvent(object):

    def __init__(self, initiator_uuid, transfer_dict):
        self.transfer = transfer_dict
        self.required_acl = 'events.transfers.{}'.format(initiator_uuid)

    def marshal(self):
        return self.transfer

    @classmethod
    def unmarshal(cls, msg):
        return cls(None, msg)

    def __eq__(self, other):
        return self.transfer == other.transfer

    def __ne__(self, other):
        return self.transfer != other.transfer


class CreateTransferEvent(BaseTransferEvent):

    name = 'transfer_created'
    routing_key = 'calls.transfer.created'


class AnswerTransferEvent(BaseTransferEvent):
    name = 'transfer_answered'
    routing_key = 'calls.transfer.edited'


class CancelTransferEvent(BaseTransferEvent):
    name = 'transfer_cancelled'
    routing_key = 'calls.transfer.edited'


class CompleteTransferEvent(BaseTransferEvent):
    name = 'transfer_completed'
    routing_key = 'calls.transfer.edited'


class AbandonTransferEvent(BaseTransferEvent):
    name = 'transfer_abandoned'
    routing_key = 'calls.transfer.edited'


class EndTransferEvent(BaseTransferEvent):
    name = 'transfer_ended'
    routing_key = 'calls.transfer.deleted'
