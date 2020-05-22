import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import { ListService } from '../../service/list.service'
import { Router } from '@angular/router';
import {ActivatedRoute} from '@angular/router';
@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.sass']
})
export class UpdateComponent implements OnInit {
  item
  update
  id
  constructor(private listService:ListService,private router: Router,private route: ActivatedRoute) {  }

  ngOnInit(): void {
    this.id=this.route.snapshot.params.id
    this.get(this.route.snapshot.params.id)
    this.generate_form()
  }
  private get(id){
    this.listService.get(id).subscribe(el => {
      this.item = el;
    });
  }
  private generate_form(){
    console.log(this.item)
    this.update=new FormGroup({
      name: new FormControl('fewf'),
    });
  
  }
  onSubmit(){
    this.listService.update(this.update.value,this.id).subscribe(el => {
      this.router.navigate(['/']);
    });
  }

}
