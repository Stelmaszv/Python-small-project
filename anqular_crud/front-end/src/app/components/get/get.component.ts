import { Component, OnInit  } from '@angular/core';
import { ListService } from '../../service/list.service'
import {ActivatedRoute} from '@angular/router';
@Component({
  selector: 'app-get',
  templateUrl: './get.component.html',
  styleUrls: ['./get.component.sass']
})
export class GetComponent implements OnInit{
  item
  id
  constructor(private listService:ListService,private route: ActivatedRoute) { }
  ngOnInit(): void {
    this.id=this.route.snapshot.params.id
    this.get(this.route.snapshot.params.id)
  }
  get(id){
    this.listService.get(id).subscribe(el => {
      this.item = el;
    });
  }

}
