import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AnqularStartComponent } from './anqular-start.component';

describe('AnqularStartComponent', () => {
  let component: AnqularStartComponent;
  let fixture: ComponentFixture<AnqularStartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AnqularStartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AnqularStartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
