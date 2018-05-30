from account.permissions import IsStationStaff
from core.services import vote
from rest_framework.views import APIView
from rest_framework.response import Response

class BoothView(APIView):
    """
    Gets the status of each booth in a voting station.
    """
    permission_classes = (IsStationStaff,)

    def get(self, request):
        station = request.user.station

        # Fetch status from vote system
        booth_list = vote.fetch_booth_status(station.foreign_id)

        # Build response
        response = {
            'status': 'success',
            'booths': { booth.booth_id: booth.status for booth in booth_list },
        }

        # Append additional information if requested
        if request.query_params.get('initialize'):
            response['station'] = station.name
            response['description'] = station.election.description or station.description

        return Response(response)
