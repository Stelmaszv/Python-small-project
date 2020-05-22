import { Component} from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import { ListService } from '../../service/list.service'
import { Router } from '@angular/router';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.sass']
})
export class CreateComponent{
  create = new FormGroup({
    name: new FormControl(''),
  });
  constructor(private listService:ListService,private router: Router) { }
  onSubmit(){
    this.listService.add(this.create.value).subscribe(el => {
      this.router.navigate(['/']);
    });
  }
}
