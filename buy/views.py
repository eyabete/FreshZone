# Create your views here.
from django.shortcuts import render, redirect
from item.models import Item  # Import your Item model or the relevant model
from django.contrib import messages

def buy_item(request, item_id):
    if request.method == 'POST':
        # Get the item based on the item_id
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            # Handle the case where the item doesn't exist
            messages.error(request, 'Item not found.')
            return redirect('item:detail', pk=item.id)

        messages.success(request, 'Item purchased successfully.')
        return redirect('item:detail', pk=item.id)

    return render(request, 'item/buy.html', {'item_id': item_id})
